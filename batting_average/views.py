from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from django.db.models import Count, Sum, Subquery, Q, Case, When, FloatField, F
from django.db.models.functions import Cast
from django.http import JsonResponse
import json

# from .serializers import MatchSerializer
from .models import Matches, Delivery


# class MatchViewSet(viewsets.ModelViewSet):
#     queryset = Matches.objects.all().values('season').order_by('season')
#     print(queryset)
#     serializer_class = MatchSerializer

def demo(request):
    pass

def bowlers_economy(request):
    queryset = Delivery.objects.filter(match_id__season=2015, \
            is_super_over=False).values('bowler').annotate(\
            runs=Sum('batsman_runs')+Sum('wide_runs')+Sum('noball_runs')). \
            annotate(balls= Count('ball')-Count(Case(When(noball_runs__gt=0, then=1)))\
            -Count(Case(When(wide_runs__gt=0, then=1)))).annotate(economy= Cast((F('runs')/(F('balls')/6.0)), FloatField())).order_by('economy')[:10]
    # print(queryset)
    queryset = list(queryset)
    return JsonResponse(queryset, safe=False)


    

def extra_runs(request):
    queryset = Delivery.objects.filter(match_id__season=2016, \
            is_super_over=False).values('bowling_team').annotate(\
            sum=Sum('extra_runs')).order_by('sum')
    # print(queryset)
    queryset = list(queryset)
    return JsonResponse(queryset, safe=False)


def matches_won_query(request):
    queryset = Matches.objects.all().values('winner','season').annotate(count=Count('winner')).order_by('season')
    queryset = list(queryset)
    return JsonResponse(queryset, safe=False)


def matches_won(request):
    queryset = json.loads(matches_won_query(request).content)
    


def first(request):
    queryset = Matches.objects.all().values('season').annotate(count=Count('season')).order_by('season')
    queryset = list(queryset)
    return JsonResponse(queryset, safe=False)

def matches_per_season(request):
    queryset = json.loads(first(request).content)
    seasons = [i['season'] for i in queryset]
    matches = [i['count'] for i in queryset]
    return render(request, 'plot.html', {'seasons':seasons, 'matches':matches})

def home(request):
    return render(request, 'index.html')
