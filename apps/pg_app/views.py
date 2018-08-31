from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.core.urlresolvers import reverse
# from .models import *

def index(request):
    return render(request, 'pg_app/index.html')