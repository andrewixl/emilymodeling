# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Photo, Home

from django.shortcuts import render, redirect, HttpResponse

def index(request):
    images = Home.objects.all()
    context = {
    "image" : images
    }
    return render(request, 'modeling/index.html', context)

def about(request):
    return render(request, 'modeling/about.html')

def portfolio(request):
    return render(request, 'modeling/portfolio.html')

def book(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect("/login")
    return render(request, 'modeling/book.html')

def contact(request):
    return render(request, 'modeling/contact.html')

def account(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect("/login")
    return render(request, 'modeling/account.html')
