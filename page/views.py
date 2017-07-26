from django.shortcuts import render
from . import markov

def main(request):
	chain = markov.init()
	word = markov.make_word(chain)
	return render(request, './page/main.html', {"word": word})