from django.http import HttpResponse
import json
import os
from hearthstone.models import Hero, Minion, Spell

def index(request):
    if not Hero.objects.all():
        module_dir = os.path.dirname(__file__)  # get current directory
        file_path = os.path.join(module_dir, 'cards.json')
        with open(file_path) as f:
            data = json.load(f)

        for card in data["Basic"]:
                if card["type"] == "Spell" or card["type"] == "Enchantment":

                    Spell.objects.create(
                        name=card.get("name"),
                        playerClass=card.get("playerClass"),
                        cost=card.get("cost",0)
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
                    rarity= card.get("rarity",0)
                )
                

    return HttpResponse("G g .")