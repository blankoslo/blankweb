from django.shortcuts import render

from .models import Employee

def index(request):
    all_employees = Employee.objects.all()
    context = {'all_employees': all_employees}
    return render(request, 'web/index.html', context)
