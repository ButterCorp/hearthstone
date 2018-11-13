from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils import timezone

#Initiating user-profile with 200 CDTS
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    credit = models.IntegerField(default=200)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Deck(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Hero(models.Model):
    name = models.TextField(max_length=30, blank=False)
    playerClass = models.TextField(max_length=50, blank=False, default="NaN")

    def __str__(self):
        return self.name

class Minion(models.Model):
    name = models.TextField(max_length=50, blank=False)
    cost = models.IntegerField(default=0)
    attack = models.IntegerField()
    health = models.IntegerField()
    rarity = models.TextField(max_length=30, blank=True)
    playerClass = models.TextField(max_length=50, blank=False)

class Spell(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=50, blank=False)
    cost = models.IntegerField(default=0)
    playerClass = models.TextField(max_length=50, blank=False)

class UserHero(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)

class UserMinion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    minion = models.ForeignKey(Minion, on_delete=models.CASCADE)

class UserSpell(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    spell = models.ForeignKey(Spell, on_delete=models.CASCADE)

class DeckHero(models.Model):
    deck = models.ForeignKey(Deck, on_delete=models.DO_NOTHING)
    hero = models.ForeignKey(Hero, on_delete=models.DO_NOTHING)

class DeckMinion(models.Model):
    deck = models.ForeignKey(Deck, on_delete=models.DO_NOTHING)
    minion = models.ForeignKey(Minion, on_delete=models.DO_NOTHING)

class DeckSpell(models.Model):
    deck = models.ForeignKey(Deck, on_delete=models.DO_NOTHING)
    spell = models.ForeignKey(Spell, on_delete=models.DO_NOTHING)
    
class Party(models.Model):
    attaquant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Attaquant')
    defenseur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Defenseur')
    gagnant = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.gagnant.username
