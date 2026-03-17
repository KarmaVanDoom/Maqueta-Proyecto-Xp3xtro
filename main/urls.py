from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('musica/', views.music_view, name='music'),
    path('contacto/', views.contact_view, name='contact'),
]
