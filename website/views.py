from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from services.models import SiteInfo, SocialAccount, Presentation, UserAccount, OtherInfo
from .models import Acceille, Contact, Fashion, Gallerie, NewsLetter
from blog.models import Tag, CategorieArticle, Article
# Create your views here.

def index(request):

    acceille = Acceille.objects.filter(status=True)[:3]
    fashion = Fashion.objects.filter(status=True)[:3]
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
    
    data = {
        
    }
    
    return render(request, 'pages/contact.html', data)  