 # Philosophie Django
 
 Installation sur windows, suivre ce tutoriel docker pour ne pas s'embourber avec les endpoints :
 https://docs.docker.com/compose/django/
 
 Quelle est la différence entre un projet et une app : 
 >Une app est un service web. Ex : Un poll, un tweet, etc. Un projet est un ensemble d'appps.

 Pour créer une app il faut lancer la commande (et être dans le même dossier que manage.py):

    python manage.py startapp nomdelapp

Les Url des différentes apps sont souvent sous la dénomination hearthstone/app/...
Du coup à la racine hearthstone je peux ajouter dans url.py mes urls de post par ex:

    path('posts/', include('posts.urls')),

En gros django nous aide à mieux factoriser notre code, et c'est une bonne pratique. 

 # Base de Données 
 ## Migrations BDD :
 
>
	python manage.py makemigrations`
	python manage.py migrate

## Filtres & Tips :

Utiliser le shell pour test et importer le(s) Model à utiliser:

	python manage.py shell
	from manapy.models import Task


Affichage :

    Post.objects.all()
    Post.objects.get(titre="Salut")
    Post.objects.filter(auteur="le King")
    Post.objects.exclude(auteur="le King")

Pour la date on importe timezone, et on peut utiliser le double underscore pour séparer les relations

    from django.utils import timezone
	Post.objects.filter(created_at__lt=timezone.now()) 

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



