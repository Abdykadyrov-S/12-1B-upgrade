from django.shortcuts import render, redirect
from .models import *
from apps.telegram_bot.views import get_text

# Create your views here.
def index(request):
    settings = Settings.objects.latest('id')
    return render(request, 'base/index.html', locals())

def about(request):
    settings = Settings.objects.latest('id')
    about = About.objects.latest('id')
    return render(request, 'base/about.html', locals())

def contact(request):
    settings = Settings.objects.latest('id')
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        cause = request.POST.get('cause')
        message = request.POST.get('message')
        Contact.objects.create(name=name, email=email, phone=phone, cause=cause, message=message)
        
        get_text(f"Оставлен отзыв от пользователя {name} \nНомер телефона: {phone} \nПричина: {cause} \nСообщение: {message}")
        return redirect("index")

    return render(request, 'base/contact.html', locals())