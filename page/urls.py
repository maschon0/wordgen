from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^a_tale_of_two_cities$', views.main(book='a_tale_of_two_cities'), name='main'),
    url(r'^alice_in_wonderland$', views.main(book='alice_in_wonderland'), name='main'),
    url(r'^descent_of_man$', views.main(book='descent_of_man'), name='main'),
    url(r'^dracula$', views.main(book='dracula'), name='main'),
    url(r'^frankenstein$', views.main(book='frankenstein'), name='main'),
    url(r'^great_expectations$', views.main(book='great_expectations'), name='main'),
    url(r'^huckleberry_finn$', views.main(book='huckleberry_finn'), name='main'),
    url(r'^on_liberty$', views.main(book='on_liberty'), name='main'),
    url(r'^origin_of_species$', views.main(book='origin_of_species'), name='main'),
    url(r'^pride_and_prejudice$', views.main(book='pride_and_prejudice'), name='main'),
    url(r'^sense_and_sensibility$', views.main(book='sense_and_sensibility'), name='main'),
    url(r'^the_brothers_karamazov$', views.main(book='the_brothers_karamazov'), name='main'),
    url(r'^tom_sawyer$', views.main(book='tom_sawyer'), name='main'),
    url(r'^voyage_of_the_beagle$', views.main(book='voyage_of_the_beagle'), name='main'),
    url(r'^war_and_peace$', views.main(book='war_and_peace'), name='main'),
]