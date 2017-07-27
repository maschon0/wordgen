# encoding: utf-8
import string
import random
import copy
from decimal import *
import json
import sys,os,re,math

library_folder = 'project_gutenberg'
markov_folder = 'markov_models'

tail_length = 2
def associate(markov, tail, head):
    if not tail in markov:
        markov[tail] = {}
        markov[tail]['_total'] = 0
    if not head in markov[tail]:
        markov[tail][head] = 1
    else:
        markov[tail][head] += 1
    markov[tail]['_total'] += 1

def train(training_array,dump=False,output_file='result.json'):
    print('training...')
    markov = {}
    # Load training data from training_array
    for sentence in training_array:
        tail = ''
        for word in sentence.split(' '):
            associate(markov, tail, word)
            tail += ' '+word
            tail = tail.strip()
            if len(tail.split(' ')) > tail_length:
                tail = ' '.join([i.strip() for i in tail.split(' ')[1:]]).strip()
        associate(markov, tail, '_end')
    if dump:
        print('trained. Dumping json')
        with open(output_file, 'w') as fp:
            json.dump(markov, fp)
        print('dumped.')        
    return markov

def guess_next(markov, tail, length, pad_length=15):
    distr = copy.deepcopy(markov[tail])
    total = Decimal(distr['_total'])
    del distr['_total']

    if not tail in markov.keys():
        return '_end'

    # Pad _end and _total based on length to limit very long words
    if length > pad_length and '_end' in distr.keys():
        end_weight = Decimal((length / float(pad_length))**1) * total
        distr['_end'] += end_weight
        total += end_weight
    
    selector_value = Decimal(random.random())
    for key in distr:
        weight = distr[key] / total
        selector_value -= weight
        if selector_value < 0:
            return key

def make_sentence(markov):
    sentence = ''
    tail = ''
    next = ''
    
    while next != '_end':
        next = guess_next(markov, tail, len(sentence))
        
        if next != '_end':
            sentence += ' '+next
            tail += ' '+next
            tail = tail.strip()
            
            if len(tail.split(' ')) > tail_length:
                tail = ' '.join([i.strip() for i in tail.split(' ')[1:]]).strip()
    
    return sentence.strip()

'''
READING A BOOK:
    1) Open a book.
    2) Read lines into the string until an empty line is reached.
    3) Flatten the text (all lowercase, replace all whitespace with single spaces, replace all clause delimiters with ',', etc.)
    4) Train a Markov chain on each sentence.
'''
word_graph    = {}
whitespace    = '[ \t\n\r\x0b\x0c\*_-]+'
specialchar   = '[^A-Za-z0-9\. ]'
sentencemarks = '[\.!\?]+'
def words_in(text):
    return re.findall(r"[\w']+",text)

def read_book(bookfile,update_master=True,dump=False,output_file='result.json'):
    book = open(library_folder+'/'+bookfile,'rb')
    output_file = markov_folder+'/'+output_file
    paragraph = ''
    book_sentences = []
    line_num=0
    for line in book:
        line=line.decode('utf-8',errors='ignore').strip()
        line_num+=1
        line = line.rstrip().lower()
        if line == '':
            if not paragraph:
                continue
            #Execute operations on a completed paragraph
            paragraph = re.sub(whitespace,' ',paragraph)
            paragraph = re.sub(specialchar,'',paragraph)
            paragraph = re.sub(sentencemarks,'.',paragraph)
            all_words = words_in(paragraph)
            sentences = paragraph.split('.')
            sentences = [s.strip() for s in sentences if len(words_in(s))>1]
            book_sentences += sentences
            paragraph = ''
        else:
            paragraph+=' '+line
        if line_num%1000 == 0:
            print("Lines processed: "+str(line_num))
    markov = train(book_sentences,dump=dump,output_file=output_file)
    x = markov.copy()
    master_markov.update(x)
    return markov

master_markov = dict()

def load_markov_from_json(json_file='result.json'):
	return eval(open(json_file).readline())

    
books = [f for f in os.listdir(library_folder) if os.path.isfile(os.path.join(library_folder,f))]
book_markovs = dict()
for book in books:
    bookname=book.split('.')[0]
    book_markovs[bookname] = read_book(book,dump=True,output_file=bookname+'.json')

with open(markov_folder+'/master_markov.json', 'w') as fp:
    print('Fully trained on library. Dumping master json...')
    json.dump(master_markov, fp)
    print('All Markovs dumped.')
    
