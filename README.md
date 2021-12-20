

# Mise en place de l'environnement virtuel sur Windows 10

    pip3 install virtualenvwrapper-win
#### Créer un environnement virtuel
Maintenant que vous avez installé  _virtualenvwrapper_  ou  _virtualenvwrapper-win_  , travailler avec des environnements virtuels sera une tâche très similaire entre chaque plateforme.

Vous pouvez désormais créer un nouvel environnement virtuel avec la commande  `mkvirtualenv`. Lors de son exécution, vous pourrez voir l'environnement être configuré (ce que vous verrez changera légèrement en fonction de votre plateforme). Lorsque l'exécution de la commande sera terminée, votre environnement virtuel sera actif — vous pouvez voir au début de la ligne de commande le nom de votre environnement entre parenthèses (nous vous montrons le résultat pour Ubuntu ci-dessous, mais la dernière ligne est similaire sur Windows/macOS).

    mkvirtualenv le_nom_de_ton_environement

# Activer l'environnement virtuel spécifié

    workon le_nom_de_ton_environement

## Installer Django

    python -m ensurepip 
    python -m pip install --upgrade pip 
    python -m pip install Django==2.1.5

## Installer les autres éléments et regarder dans requirements.txt

    python -m pip install django-tinymce4-lite 
    pip install django-crispy-forms



## Lancer le Project

    python manage.py runserver
 En cas de problèmes aller dans settings.py et supprimer dans INSTALLED_APPS la ligne problématique 

**Source**: https://developer.mozilla.org/fr/docs/Learn/Server-side/Django/development_environment
