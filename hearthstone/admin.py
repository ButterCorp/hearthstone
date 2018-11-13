from django.contrib import admin

# Register your models here.
from .models import Deck, Hero, Minion, Spell, Party

admin.site.register(Deck)
admin.site.register(Minion)
admin.site.register(Hero)
admin.site.register(Spell)
admin.site.register(Party)