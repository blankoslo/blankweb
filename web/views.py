from django.shortcuts import render
from django.http import HttpResponse
import requests

from .models import Employee, JobPostingCategory

POSTINGS_ROOT = 'https://api.lever.co/v0/postings/blankoslo'

def index(request):
    all_employees = Employee.objects.order_by('?').all()
    context = {'all_employees': all_employees, 'color_classes': ['bgblue', 'bgred', 'bgyellow']}
    return render(request, 'web/index.html', context)

def posting(request, posting_id):
    posting_dict = requests.get(POSTINGS_ROOT + '/' + posting_id).json()
    team = posting_dict['categories']['team'].lower()
    context = {'posting':posting_dict, 'category': JobPostingCategory.objects.filter(team=team)[0]}
    return render(request, 'web/posting.html', context)

def team_postings(request, team):
    postings_array = requests.get(POSTINGS_ROOT + '?team=' + team + '&mode=json').json()
    context = {'team_postings' :  postings_array, 'category': JobPostingCategory.objects.filter(team=team)[0], 'team' : team}
    return render(request, 'web/postings.html', context)

def team_design(request):
    postings_array = requests.get(POSTINGS_ROOT + '?team=' + 'brukeropplevelse' + '&mode=json').json()
    context = {'team_postings' :  postings_array, 'category': JobPostingCategory.objects.filter(team='brukeropplevelse')[0], 'team' : 'brukeropplevelse'}
    return render(request, 'web/design.html', context)

def team_teknologi(request):
    postings_array = requests.get(POSTINGS_ROOT + '?team=' + 'teknologi' + '&mode=json').json()
    context = {'team_postings' :  postings_array, 'category': JobPostingCategory.objects.filter(team='teknologi')[0], 'team' : 'teknologi'}
    return render(request, 'web/teknologi.html', context)
