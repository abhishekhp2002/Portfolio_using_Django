from django.shortcuts import render
from django.http import HttpResponse
from Base import models

from django.core.mail import send_mail
# Create your views here.
def home(request):
    return render(request,'home.html')
