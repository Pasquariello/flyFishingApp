from django.urls import path

from . import views
from .views import create_league_with_rivers, gameDetails, riverDetails, userProfile
app_name = 'flyFishing'
urlpatterns = [
    path('', views.index, name='index'),
    path('create-league/', views.create_league_with_rivers, name='create-league'),
    path('game-details/<int:league_id>/', views.gameDetails, name='gameDetails'),
    path('edit-river-details/<int:river_id>/', views.riverDetails, name='edit-river-details'),
    path('league-list/', views.leagueList, name='league-list'),
    path('user-profile/', views.userProfile, name='user-profile'),


]