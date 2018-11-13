from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='app_login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='app_logout'),
    path('party/', views.party, name='game'),
    path('hero/<int:hero_id>', views.hero, name='hero'),
    path('sell-hero/<int:herouser_id>', views.sellHero, name='sellHero'),
    path('buy-heroes/', views.buyHero, name='buyHero'),
    path('my-cards/', views.myHeroes, name='myCards'),
    path('my-decks/', views.myDecks, name='myDecks'),
    path('deck/<int:deck_id>', views.deck, name='deck'),
    path('deck/delete/<int:deck_id>', views.deleteDeck, name='deckDelete'),
    path('deck/update/<int:deck_id>', views.updateDeck, name='deckUpdate'),
    path('deck/create', views.createDeck, name='deckCreate'),
    path('deck/create/<int:hero_id>', views.createDeckByHero, name='createDeckByHero'),
]