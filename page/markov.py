import string
import random
import copy
from decimal import *

json_dir='markov_models/'
def init(book='huckleberry_finn'):
	return eval(open(json_dir+book+'.json').readline())

tail_length = 2

def guess_next(markov, tail):
	distr = copy.deepcopy(markov[tail])
	total = Decimal(distr['_total'])
	del distr['_total']
	
	if not tail in markov:
		return '_end'
	
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
