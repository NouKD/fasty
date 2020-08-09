from django.shortcuts import render, redirect
from django.core.validators import EmailValidator
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.models import User
from services.models import SiteInfo, SocialAccount, Presentation, UserAccount, OtherInfo
from .models import Acceille, Contact, Fashion, Gallerie, NewsLetter
from blog.models import Tag, CategorieArticle, Article
from .forms import ContactForm
# Create your views here.

def index(request, filtre=None, id=None):

    articles = Article.objects.filter(status=True)[:6]

    _paginator = Paginator(articles, 9)
    page = request.GET.get('page')

    acceille = Acceille.objects.filter(status=True)[:3]
    fashion = Fashion.objects.filter(status=True)[:4]
    gallerie = Gallerie.objects.filter(status=True)[:10]
    tags = Tag.objects.filter(status=True)[:6]

    try:
        articles_page = _paginator.page(page)
    except PageNotAnInteger: # Si le numero de page n'est pas un entier
        articles_page = _paginator.page(1)
    except EmptyPage: # Si la page est vide
        articles_page = _paginator.page(_paginator.num_pages)

    data = {
        'acceille': acceille,
        'fashion': fashion,
        'gallerie': gallerie,
        'tags': tags, 
        'articles': articles, 
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
    tags = Tag.objects.filter(status=True)[:6]
    articles = Article.objects.filter(status=True)
    newsletter = NewsLetter.objects.filter(status=True).last
    contact_form = ContactForm(request.POST or None)
    
    if request.method == 'POST':
        if contact_form.is_valid():
            contact_form.save()
            contact_form = ContactForm()

    data = {
        'tags': tags, 
        'articles': articles,
        'newsletter': newsletter,
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