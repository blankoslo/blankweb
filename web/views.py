from django.shortcuts import render
from django.http import HttpResponse
import requests

from .models import Employee

POSTINGS_ROOT = 'https://api.lever.co/v0/postings/blankoslo'

TECH_TEAM = 'Teknologi'
DESIGN_TEAM = 'Brukeropplevelse'
BUSINESS_TEAM = 'Forretningsdesign'

def index(request):
    all_employees = Employee.objects.all()
    context = {'all_employees': all_employees}
    return render(request, 'web/index.html', context)

def posting(request, posting_id):
    def get_template(team):
        return {
            TECH_TEAM : 'web/posting_tech.html',
            DESIGN_TEAM : 'web/posting_design.html',
            BUSINESS_TEAM : 'web/posting_business.html',
        }.get(team, 'web/posting_business.html')

    posting_dict = requests.get(POSTINGS_ROOT + '/' + posting_id).json()
    template = get_template(posting_dict['categories']['team'])
    context = {'text': posting_dict['text'], 'description': posting_dict['description']}

    return render(request, template, context)
