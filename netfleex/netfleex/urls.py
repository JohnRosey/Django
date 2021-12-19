
from django.contrib import admin
from django.urls import path, include
from users import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),# le chemin qui est dans path '' renvoie vers le fichier urls.py du dossier core
    path('register/',views.register, name='register'),
]
