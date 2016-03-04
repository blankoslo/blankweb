from django.shortcuts import render
from django.http import HttpResponse
import requests

from .models import Employee

POSTINGS_ROOT = 'https://api.lever.co/v0/postings/blankoslo';

def index(request):
    all_employees = Employee.objects.all()
    context = {'all_employees': all_employees}
    return render(request, 'web/index.html', context)

def posting(request, posting_id):
    r = requests.get(POSTINGS_ROOT + '/' + posting_id)
    return render(request, 'web/posting.html', r.json())
