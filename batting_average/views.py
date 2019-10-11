from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from django.db.models import Count, Sum, Subquery, Q, Case, When, FloatField, F
from django.db.models.functions import Cast
from django.http import JsonResponse
import json
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)
from django.forms import ModelForm

# from .serializers import MatchSerializer
from .models import Matches, Delivery


# class MatchViewSet(viewsets.ModelViewSet):
#     queryset = Matches.objects.all().values('season').order_by('season')
#     print(queryset)
#     serializer_class = MatchSerializer

class MatchForm(ModelForm):
    
     class Meta:
            model = Matches
            fields = __all__

def get_match(request, id):
    queryset = Matches.objects.values().get(pk=id)
    # queryset = list(queryset)
    # print(queryset.season)
    # print('1',help(queryset))
    # print('2',dir(queryset))
    # print('3',queryset.__dict__)
    # k = queryset.__dict__.keys()
    # v = queryset.__dict__.values()
    # print(v,k)

    return JsonResponse(queryset, safe=False)


@cache_page(CACHE_TTL)
def bowlers_economy(request):
    queryset = Delivery.objects.filter(match_id__season=2015, \
            is_super_over=False).values('bowler').annotate(\
            runs=Sum('batsman_runs')+Sum('wide_runs')+Sum('noball_runs')). \
            annotate(balls= Count('ball')-Count(Case(When(noball_runs__gt=0, then=1)))\
            -Count(Case(When(wide_runs__gt=0, then=1)))).annotate(economy= Cast((F('runs')/(F('balls')/6.0)), FloatField())).order_by('economy')[:10]
    queryset = list(queryset)
    bowlers = [i['bowler'] for i in queryset]
    eco = [i['economy'] for i in queryset]
    return JsonResponse({'bowlers':bowlers, 'economies':eco})


# def bowlers_economy(request):
#     queryset = json.loads(bowlers_economy_query(request).content)
#     print(queryset)
#     bowlers = [i['bowler'] for i in queryset]
#     eco = [i['economy'] for i in queryset]
#     print(bowlers, eco)
#     return render(request, 'bowlers_eco.html', {'bowlers':bowlers, \
#     'eco':eco})

@cache_page(CACHE_TTL)
def extra_runs(request):
    queryset = Delivery.objects.filter(match_id__season=2016, \
            is_super_over=False).values('bowling_team').annotate(\
            sum=Sum('extra_runs')).order_by('sum')
    queryset = list(queryset)
    teams = [i['bowling_team'] for i in queryset]
    runs = [i['sum'] for i in queryset]
    return JsonResponse({'teams': teams, 'extra_runs':runs})


# def extra_runs(request):
#     queryset = json.loads(extra_runs_query(request).content)
#     bowling_team = [i['bowling_team'] for i in queryset]
#     extra_runs = [i['sum'] for i in queryset]
#     bowling_team = JsonResponse(bowling_team,safe=False)
#     print(bowling_team)
#     return render(request, 'extra_runs.html', {'bowling_team':bowling_team.content, \
#     'extra_runs':extra_runs})

@cache_page(CACHE_TTL)
def matches_won(request):
    seasons = Matches.objects.all().values('season').order_by('season').distinct()
    teams = Matches.objects.exclude(winner=None).values('winner').order_by('winner').distinct()
    queryset = Matches.objects.exclude(winner=None).values('winner','season').annotate(count=Count('winner')).order_by('season')
    seasons_list = []
    for season in seasons:
        seasons_list.append(season['season'])
    team_with_data = {}
    for team in teams:
        team_with_data[team['winner']] = [0]*len(seasons)
    print (seasons_list, team_with_data)
    for row in queryset:
        season = row['season']
        winner = row['winner']
        count = row['count']
        team_with_data[winner][seasons_list.index(season)] = count

    team_data = []
    for data in team_with_data:
        team_data.append({'name': data, 'data': team_with_data[data]})
    data = {'season': seasons_list, 'team_data' : team_data}

    return JsonResponse(data)

# def matches_won_query(request):
    # queryset = Matches.objects.all().values('winner','season').annotate(count=Count('winner')).order_by('season')
    # queryset = list(queryset)
    # return JsonResponse(queryset, safe=False)


# def matches_won(request):
#     queryset = json.loads(matches_won_query(request).content)
#     print(queryset)
#     return render(request, 'matches_won.html')
    

@cache_page(CACHE_TTL)
def matches_per_season(request):
    queryset = Matches.objects.all().values('season').annotate(count=Count('season')).order_by('season')
    queryset = list(queryset)
    seasons = [i['season'] for i in queryset]
    matches = [i['count'] for i in queryset]
    return JsonResponse({'seasons':seasons, 'matches':matches})

# def matches_per_season(request):
#     queryset = json.loads(first(request).content)
#     seasons = [i['season'] for i in queryset]
#     matches = [i['count'] for i in queryset]
#     return render(request, 'plot.html', {'seasons':seasons, 'matches':matches})

def home(request):
    return render(request, 'index.html')
