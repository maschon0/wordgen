from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^a_tale_of_two_cities$', views.a_tale_of_two_cities, name='main'),
    url(r'^alice_in_wonderland$', views.alice_in_wonderland, name='main'),
    url(r'^descent_of_man$', views.descent_of_man, name='main'),
    url(r'^dracula$', views.dracula, name='main'),
    url(r'^frankenstein$', views.frankenstein, name='main'),
    url(r'^great_expectations$', views.great_expectations, name='main'),
    url(r'^huckleberry_finn$', views.huckleberry_finn, name='main'),
    url(r'^on_liberty$', views.on_liberty, name='main'),
    url(r'^origin_of_species$', views.origin_of_species, name='main'),
    url(r'^pride_and_prejudice$', views.pride_and_prejudice, name='main'),
    url(r'^sense_and_sensibility$', views.sense_and_sensibility, name='main'),
    url(r'^the_brothers_karamazov$', views.the_brothers_karamazov, name='main'),
    url(r'^tom_sawyer$', views.tom_sawyer, name='main'),
    url(r'^voyage_of_the_beagle$', views.voyage_of_the_beagle, name='main'),
    url(r'^war_and_peace$', views.war_and_peace, name='main'),
]