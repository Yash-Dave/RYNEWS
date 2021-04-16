from django.urls import path
from .import views

urlpatterns = [
   path('',views.home),
   path('home',views.home, name="home"),
   path('business',views.business, name="business"),
   path('tech',views.tech, name="tech"),
   path('entertainment',views.entertainment, name="entertainment"),
   path('health',views.health, name="health"),
   path('sports',views.sports, name="sports"),
   path('science',views.science, name="science"),
]
