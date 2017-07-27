import string
import random
import copy
from decimal import *

json_dir='markov_models/'
def init(book='huckleberry_finn'):
    with open(json_dir+book+'.json') as myfile:
        data=myfile.read().replace('\n', '')
    return eval(data)

tail_length = 2

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

def make_word(markov):
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
