from django.urls import path, include
from . import views
# from rest_framework import routers


# router = routers.DefaultRouter()
# router.register(r'matches', views.MatchViewSet)

app_name = 'batting_average'
urlpatterns = [
    path('', views.home),
    path('api/matches_per_season', views.matches_per_season, name='matches_per_season'),
    path('api/matches_won', views.matches_won, name='matches_won'),
    path('api/extra_runs_conceded', views.extra_runs, name='extra_runs'),
    path('api/bowlers_economy', views.bowlers_economy, name='bowlers_economy'),
    path('api/matches/<int:id>', views.get_match, name='get_match'),
    path('api/deliveries/<int:id>', views.get_deliveries, name='get_deliveries'),
    path('api/create_match', views.create_match, name='create_match'),
    path('api/create_delivery', views.create_delivery, name='create_delivery'),
    path('api/update_match/<int:id>', views.update_match, name='update_match'),
    path('api/update_delivery/<int:id>', views.update_delivery, name='update_delivery'),
]
