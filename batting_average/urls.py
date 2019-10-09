from django.urls import path, include
from . import views
# from rest_framework import routers


# router = routers.DefaultRouter()
# router.register(r'matches', views.MatchViewSet)

app_name = 'batting_average'
urlpatterns = [
    path('', views.home),
    path('matches_per_season', views.matches_per_season, name='matches_per_season'),
    path('matches_won', views.matches_won, name='matches_won'),
    path('extra_runs', views.extra_runs, name='extra_runs'),
    path('bowlers_economy', views.bowlers_economy, name='bowlers_economy'),
]
