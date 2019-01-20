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
    cards = models.TextField(blank=True) #use json.dumps(var) to insert cards
    playerClass = models.TextField(max_length=50, blank=False, default="NaN")
    finished = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Hero(models.Model):
    name = models.TextField(max_length=30, blank=False)
    playerClass = models.TextField(max_length=50, blank=False, default="NaN")

    def __str__(self):
        return self.name

class Card(models.Model):
    name = models.TextField(max_length=30, blank=False)
    playerClass = models.TextField(max_length=50, blank=False)
    cost = models.IntegerField(default=0)
    img_url = models.TextField(max_length=255, blank=True)
    rarity = models.TextField(max_length=30, blank=True)
    extension = models.TextField(max_length=60, blank=False, default="Basic")

    def __str__(self):
        return self.name

class Minion(Card):
    attack = models.IntegerField()
    health = models.IntegerField()

    def __str__(self):
        return self.name

class Spell(Card):

    def __str__(self):
        return self.name

class UserCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    
class Party(models.Model):
    attaquant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Attaquant')
    defenseur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Defenseur')
    gagnant = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.gagnant.username

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    post_content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="created")
    updated_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="updated")
    id_author = models.ForeignKey(User, on_delete=models.CASCADE,)

    def __str__(self):
        return self.id

class Follow(models.Model):
    id_follower = models.IntegerField()
    id_followed = models.IntegerField()
