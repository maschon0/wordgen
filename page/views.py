from django.shortcuts import render
from . import markov

def main(request,book='master_markov'):
    chain = markov.init(book)
    word = markov.make_word(chain)
    return render(request, './page/main.html', {"word": word})
    
def a_tale_of_two_cities(request,book='a_tale_of_two_cities'):
    chain = markov.init(book)
    word = markov.make_word(chain)
    return render(request, './page/main.html', {"word": word})
    
def alice_in_wonderland(request,book='alice_in_wonderland$'):
    chain = markov.init(book)
    word = markov.make_word(chain)
    return render(request, './page/main.html', {"word": word})
    
def descent_of_man(request,book='descent_of_man'):
    chain = markov.init(book)
    word = markov.make_word(chain)
    return render(request, './page/main.html', {"word": word})
    
def dracula(request,book='dracula'):
    chain = markov.init(book)
    word = markov.make_word(chain)
    return render(request, './page/main.html', {"word": word})
    
def frankenstein(request,book='frankenstein'):
    chain = markov.init(book)
    word = markov.make_word(chain)
    return render(request, './page/main.html', {"word": word})
    
def great_expectations(request,book='great_expectations'):
    chain = markov.init(book)
    word = markov.make_word(chain)
    return render(request, './page/main.html', {"word": word})

def huckleberry_finn(request,book='huckleberry_finn'):
    chain = markov.init(book)
    word = markov.make_word(chain)
    return render(request, './page/main.html', {"word": word})
    
def on_liberty(request,book='on_liberty'):
    chain = markov.init(book)
    word = markov.make_word(chain)
    return render(request, './page/main.html', {"word": word})
    
def origin_of_species(request,book='origin_of_species'):
    chain = markov.init(book)
    word = markov.make_word(chain)
    return render(request, './page/main.html', {"word": word})
    
def pride_and_prejudice(request,book='pride_and_prejudice'):
    chain = markov.init(book)
    word = markov.make_word(chain)
    return render(request, './page/main.html', {"word": word})
    
def sense_and_sensibility(request,book='sense_and_sensibility'):
    chain = markov.init(book)
    word = markov.make_word(chain)
    return render(request, './page/main.html', {"word": word})
    
def the_brothers_karamazov(request,book='the_brothers_karamazov'):
    chain = markov.init(book)
    word = markov.make_word(chain)
    return render(request, './page/main.html', {"word": word})
    
def tom_sawyer(request,book='tom_sawyer'):
    chain = markov.init(book)
    word = markov.make_word(chain)
    return render(request, './page/main.html', {"word": word})
    
def voyage_of_the_beagle(request,book='voyage_of_the_beagle'):
    chain = markov.init(book)
    word = markov.make_word(chain)
    return render(request, './page/main.html', {"word": word})
    
def war_and_peace(request,book='war_and_peace'):
    chain = markov.init(book)
    word = markov.make_word(chain)
    return render(request, './page/main.html', {"word": word})
    