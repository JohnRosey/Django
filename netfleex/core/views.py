from typing import ContextManager
from django.shortcuts import render
from django.http import HttpResponse
from .models import Netfeelex
from .models import Category
# Create your views here.
def home(request):
    context={
       'netfeelex': Netfeelex.objects.all(),}
    return render(request, 'home.html',context)
def about(request):
    return render(request, 'about.html')