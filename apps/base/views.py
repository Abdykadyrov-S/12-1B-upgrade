from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    settings = Settings.objects.latest('id')
    return render(request, 'base/index.html', locals())