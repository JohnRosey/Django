from typing import ContextManager
from django.shortcuts import render
from django.http import HttpResponse
from .models import Netfeelex


# Create your views here.
def home(request):
    context = {
        'netfeelex': Netfeelex.objects.all(), }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')


def search_result(request):
    if request.method == "POST":
        searched = request.POST['searched']
        netfeelex= Netfeelex.objects.filter(Titre_film__contains=searched)
        return render(request,
                      'search_result.html',
                      {'searched': searched,
                       'netfeelex':netfeelex})
    else:
        return render(request, 'search_result.html',
                      {})
