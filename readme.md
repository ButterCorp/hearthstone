 # Reproduction fidèle d'hearthstone en Django
 ## Installation
	
	docker-compose up

	docker-compose exec web python manage.py migrate

## Get started

Let's navigate to http://localhost:8000

 # Philosophie Django
 
 Installation sur windows, suivre ce tutoriel docker pour ne pas s'embourber avec les endpoints :
 https://docs.docker.com/compose/django/
 
 Quelle est la différence entre un projet et une app : 
 >Une app est un service web. Ex : Un poll, un tweet, etc. Un projet est un ensemble d'appps.

 Pour créer une app il faut lancer la commande (et être dans le même dossier que manage.py):

    docker-compose run --rm web python manage.py startapp nomdelapp

Les Url des différentes apps sont souvent sous la dénomination hearthstone/app/...
Du coup à la racine hearthstone je peux ajouter dans url.py mes urls de post par ex:

    path('posts/', include('posts.urls')),

En gros django nous aide à mieux factoriser notre code, et c'est une bonne pratique. 

 # Base de Données 
 ## Migrations BDD :
 
>
	docker-compose run --rm web python manage.py makemigrations
	docker-compose run --rm web python manage.py migrate

## Filtres & Tips :

Utiliser le shell pour test et importer le(s) Model à utiliser (ne pas oublier de migrate avant):

	docker-compose run --rm web python manage.py shell
	//le shell s'ouvre
	from polls.models import Choice, Question


Affichage :

    Question.objects.all()
    Question.objects.get(question_text = "Youyou est-il vraiment le plus fort?")
    Question.objects.filter(question_text = "Youyou est-il vraiment le plus fort?")
    Question.objects.exclude(auteur="Youyou est-il vraiment le plus fort?")

Pour la date on importe timezone, et on peut utiliser le double underscore pour séparer les relations

    from django.utils import timezone
	q.pub_date = timezone.now()

>lt = less than |gt = greater than

One-two-many:

	cat.article_set.all() //on rajoute _set

many-to-many:

	task1.users.add(user1,user2) //ajoute 2 users sur une tache
	user1.tasks_set.all() //recupere toutes les taches de users1

# Vues:

	return redirect(view_article, id_article=42)
	redirige vers la vue article et donne en parametre id_article=42

	url(r'^article/(?P<id_article>\d+)$', views.view_article, name="afficher_article")

Le parametre name="" permet de nommer la vue. (namespace?)
donc on peut utiliser après le redirect : return redirect('afficher_article', id_article=42)

Notes sur les vues  : 

	{{ texte|truncatewords:80 }} : tronque la variable text 80 char
	message{{ nb_messages|pluralize }} : rajoute un s si nb_messages > 1


Boucles et conditions :

IF ELSE:

	{% if sexe == "Femme" %}
   		Madame
	{% else %}
   		Monsieur
	{% endif %}

FOR :

	{% for couleur in couleurs %}
    		<li>{{ couleur }}</li>
	{% empty %}
		MESSAGE AFFICHE SI LA LISTE EST VIDE.
	{% endfor %}

FOR:

	{% for code, nom in couleurs.items %} # TOUJOURS FINIR AVEC .items pour les dico.
    		<li style="color:#{{ code }}">{{ nom }}</li>
	{% endfor %}

## A faire pour la soutenance:

> - échanger des cartes avec un autre joueur (troc)

> - vendre des cartes

> - jouer contre un autre joueur

> - jouer contre un personnage non joueur, préconfiguré par l'administrateur

> - suivre d'autres joueurs (vous aurez alors des informations sur leurs dernières actions dans votre flux
d'actualité)

> - discuter avec d'autres membres via des forums

> - voir sa collection, et celle des autres joueurs

> Des points seront attribués en plus si le serveur est mis en ligne.


