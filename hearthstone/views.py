from django.http import HttpResponse
import json
import os
from hearthstone.models import Hero, Minion, Card, Spell, Deck, Party, UserCard
from random import randint
from pprint import pprint
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from .forms import UserRegisterForm
from .forms import DeckForm
from django.contrib import messages
from django.contrib.auth import authenticate, login

def index(request):
    if not Hero.objects.all():
        module_dir = os.path.dirname(__file__)  # get current directory
        file_path = os.path.join(module_dir, 'cards.json')
        with open(file_path) as f:
            data = json.load(f)

        for card in data["Basic"]:
                #enchantements not used
                if card["type"] == "Spell":

                    Spell.objects.create(
                        name=card.get("name"),
                        playerClass=card.get("playerClass"),
                        cost=card.get("cost",0),
                        img_url=card.get("img", "https://i.imgur.com/U1dkXzQ.png"),
                        rarity= card.get("rarity","NAN"),
                    )

                elif card["type"] == "Hero":

                    Hero.objects.create(
                        name=card.get("name"),
                        playerClass=card.get("playerClass")
                    )

        decks = ["Basic","Classic","Naxxramas","Goblins vs Gnomes","The Grand Tournament"]
        for deck in decks:
                    
            for card in data[deck]:
                if card["type"] != "Minion":
                    continue

                Minion.objects.create(
                    name=card.get("name"),
                    cost=card.get("cost",0),
                    attack=card.get("attack",0),
                    health=card.get("health",1),
                    playerClass=card.get("playerClass"),
                    rarity= card.get("rarity","NAN"),
                    img_url=card.get("img","https://i.imgur.com/U1dkXzQ.png"),
                )
                
    return render(request, 'hearthstone/index.html')

def home(request):
    title = 'Accueil'
    context = {
        'title': title,
        'parties': Party.objects.all(),
        'Hero': Hero.objects.all(),
    }
    return render(request, 'hearthstone/index.html', context)


def register(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hello {username}, votre compte a bien été créé !')
            new_user = authenticate(
                username = username,
                password=form.cleaned_data['password1'],
            )
            login(request, new_user)
            for c in Card.objects.filter(rarity="Free"):
                UserCard.objects.create(user = new_user, card = c)
        
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})

def party(request):
    return render(request, 'hearthstone/party.html')

def buyCards(request):
    Minions = Minion.objects.all().count()
    heroes = []
    if request.user.is_authenticated and request.user.profile.credit >= 100:
        for i in range(8):
            random_index = randint(0, heroCounter - 1)
            hero = Minion.objects.all()[random_index]
            heroes.append(hero)
            userHero = UserMinion(user=request.user, minion = hero)
            userHero.save()
        request.user.profile.credit -= 100
        request.user.save()
    elif request.user.is_authenticated and request.user.profile.credit < 100:
        messages.warning(request, f'Vous n\'avez pas assez de crédit :(')
        return redirect('home')
    else:
        messages.warning(request, f'Vous devez être connecté pour accéder à cette page')
        return redirect('home')

    return render(request, 'hearthstone/buy-heroes.html', {'heroes': heroes})

def sellCard(request, carduser_id):
    card = get_object_or_404(CardUser, pk=carduser_id)
    card.delete()
    request.user.profile.credit += 10
    request.user.save()
    return redirect('myCards')


def myCards(request):
    userHeroes = UserHero.objects.all().filter(user_id=request.user.id)
    myHeroes = []

    for userHero in userHeroes:
        hero = userHero.hero
        myHeroes.append(hero)

    return render(request, 'hearthstone/my-heroes.html', {'heroes': myHeroes})


def myDecks(request):
    decksUser = Deck.objects.all().filter(user_id=request.user.id)

    return render(request, 'hearthstone/my-decks.html', {'decks': decksUser})


def deck(request, deck_id):
    deck = get_object_or_404(Deck, pk=deck_id)

    cardsDeck = CardDeck.objects.all().filter(deck_id=deck_id)
    cards = []

    for card in cardsDeck:
        cards.append(card.card)

    return render(request, 'hearthstone/deck.html', {'cards': cards, 'deck': deck})


def createDeck(request):

    heros = Hero.objects.all()

    return render(request, 'hearthstone/create-deck.html', {'heros': heros})

def createDeckByHero(request, hero_id):

    hero = Hero.objects.get(pk=hero_id)
    minions = Minion.objects.filter(playerClass__in=[hero.playerClass, 'Neutral'])
    spells = Spell.objects.filter(playerClass__in=[hero.playerClass, "Neutral"])

    if request.POST:
        form = DeckForm(request.POST)
        if form.is_valid():
            deck = Deck()
            deck = form.save(commit=False)
            deck.user = request.user
            deck.save()

            title = form.cleaned_data.get('title')
            messages.success(request, f'Le deck {title} a bien été créé !')

            return redirect('deck', deck.pk)
    else:
        form = DeckForm()

    return render(request, 'hearthstone/create-deck-by-hero.html', {'form': form, 'minions': minions, 'spells': spells, 'hero': hero.playerClass})
    


def deleteDeck(request, deck_id):
    deck = get_object_or_404(Deck, pk=deck_id)

    deck.delete()

    return redirect('myDecks')


def updateDeck(request, deck_id):
    if request.POST:
        deck = get_object_or_404(Deck, pk=deck_id)
        cards = request.POST.items()

        cardDeck = CardDeck.objects.all().filter(deck_id=deck_id)

        for cardDeck in cardDeck:
            cardDeck.delete()

        for key, value in cards:
            if key[:4] == 'card':
                cardId = key.split('_')[1]

                card = get_object_or_404(Card, pk=cardId)

                cardDeck = CardDeck(card=card, deck=deck)
                cardDeck.save()

        return redirect('deck', deck.pk)
    else:
        deck = get_object_or_404(Deck, pk=deck_id)

        cardsUser = CardUser.objects.all().filter(user_id=request.user.id)
        cards = []

        cardsDeck = CardDeck.objects.all().filter(deck_id=deck_id)
        cardsUsed = []

        for card in cardsDeck:
            cardsUsed.append(card.card.pk)

        for cardUser in cardsUser:
            card = cardUser.card
            cards.append(card)

        return render(request, 'hearthstone/update-deck.html', {'cards': cards, 'deck': deck, 'cardsUsed' : cardsUsed})

