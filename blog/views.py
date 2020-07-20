from django.shortcuts import  render, redirect, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.models import User
from services.models import SiteInfo, SocialAccount, Presentation, UserAccount, OtherInfo
from blog.models import CategorieArticle, Tag, Article, Commentaire
from django.db.models import Q

# Create your views here.

def blog(request, filtre=None, id=None):
    
    if filtre == 'categories':
        articles = Article.objects.filter(status=True, categorie=id)
    elif filtre == 'tag':
        articles = Article.objects.filter(status=True, tag=id)
    else:
        articles = Article.objects.filter(status=True)

    _paginator = Paginator(articles, 9)
    page = request.GET.get('page')

    tags = Tag.objects.filter(status=True)[:6]
    categories = CategorieArticle.objects.filter(status=True)[:9]
    info_site = SiteInfo.objects.filter(status=True)[:3]
    social_account = SocialAccount.objects.filter(status=True)[:1]

    try:
        articles_page = _paginator.page(page)
    except PageNotAnInteger: # Si le numero de page n'est pas un entier
        articles_page = _paginator.page(1)
    except EmptyPage: # Si la page est vide
        articles_page = _paginator.page(_paginator.num_pages)

    

    data = {
        'articles': articles_page,
        'tags': tags,
        'categories': categories,
        'recent_articles': articles.order_by('-date_update')[:6],
        'info_site': info_site,
        'social_account': social_account,
    }

    return render(request, 'pages/blog.html', data)

def single_blog(request, article_id):
    
    article = get_object_or_404(Article, status=True, pk=article_id)
    articles_recent = Article.objects.filter(status=True).order_by('-date_update')[:4]
    tags = Tag.objects.filter(status=True)[:9]
    commentaires =  Commentaire.objects.filter(status=True)
    categories = CategorieArticle.objects.filter(status=True).last
    autresInfo = OtherInfo.objects.filter(status=True).last

    if request.method == 'POST' and request.POST['comment']:
        if request.user.is_authenticated:
            new_comment = Commentaire.objects.create(
                commentaire=request.POST['comment'],
                auteur=request.user,
                article=article
            )
            new_comment.save()
        else:
            return redirect('login')

    data = {
        
        'l_article': article,
        'next_article': article.get_previous_by_date_update,
        'prev_article': article.get_next_by_date_update,
        'articles_recent': articles_recent,
        'tags': tags,
        'commentaires': commentaires,
        'categories': categories,
        'autresInfo': autresInfo,
    }
    return render(request, "pages/single-blog.html", data)

def search(request):
    try:
        request.POST['search']
        assert len(request.POST['search']) >= 2
    except Exception:
        return redirect(request.META.get('HTTP_REFERER', '/'))

    q = request.POST['search']
    articles = Article.objects.filter(status=True)
    articles = articles.filter(Q(titre__icontains=q) | Q(description__icontains=q) | Q(contenu__icontains=q))

    data = {
        'q': q,
        'articles': articles,
        'nombre_resultat': len(articles),
    }

    return render(request, 'pages/blog_search.html', data)