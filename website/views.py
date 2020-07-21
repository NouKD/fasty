from django.shortcuts import render, redirect
from django.core.validators import EmailValidator
from django.contrib.auth.models import User
from services.models import SiteInfo, SocialAccount, Presentation, UserAccount, OtherInfo
from .models import Acceille, Contact, Fashion, Gallerie, NewsLetter
from blog.models import Tag, CategorieArticle, Article
from .forms import ContactForm
# Create your views here.

def index(request, filtre=None, id=None):

    acceille = Acceille.objects.filter(status=True)[:3]
    fashion = Fashion.objects.filter(status=True)[:4]
    gallerie = Gallerie.objects.filter(status=True)[:10]

    data = {
        'acceille': acceille,
        'fashion': fashion,
        'gallerie': gallerie,  
    }
    
    return render(request, 'pages/index.html', data)

def about(request):
    presentation = Presentation.objects.filter(status=True).last
    newsletter = NewsLetter.objects.filter(status=True).last

    data = {
        'presentation': presentation,
        'newsletter': newsletter,
    }
    
    return render(request, 'pages/abou.html', data) 

def contact(request):
    contact_form = ContactForm(request.POST or None)
    
    if request.method == 'POST':
        if contact_form.is_valid():
            contact_form.save()
            contact_form = ContactForm()

    data = {
        'contact_form': contact_form
    }
    
    return render(request, 'pages/contact.html', data) 

def news_letter(request):
    if request.method == 'POST':
        newsletter = request.POST.get('newsletter')
        if newsletter:
            nl = NewsLetter.objects.create(mail=newsletter)
            nl.save()
    return redirect(request.META.get('HTTP_REFERER', '/'))  