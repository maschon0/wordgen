from django.shortcuts import render
from . import markov

def main(request,book='huckleberry_finn'):
	chain = markov.init(book)
	word = markov.make_word(chain)
	return render(request, './page/main.html', {"word": word})