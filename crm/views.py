"""
crm/views.py
CRM app views.
"""
from django.http import HttpResponse


def index(request):
    return HttpResponse('Index Page.')
