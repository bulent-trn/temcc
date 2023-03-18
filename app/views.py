from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from .models import Blog, Category, Product, Portfolio, Hizmetler, Kurumsal
from taggit.managers import TaggableManager
from django.db.models import Q
from django.core.paginator import Paginator
from math import *



def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    last_four=Blog.objects.filter(is_home=True, is_active=True).order_by('-id')[:4]
    products=Product.objects.filter(is_home=True, is_active=True)
    return render(
        request,
        'app/index.html',
        {
            'products':products,
            'last_four':last_four,
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    last_four=Blog.objects.filter(is_home=True, is_active=True).order_by('-id')[:4]
    return render(
        request,
        'app/contact.html',
        {
            'last_four':last_four,
            'title':'Contact',
            'message':'TEMCO Mühendislik İletişim ',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'TEMCO Mühendislik',
            'year':datetime.now().year,
        }
    )

def portfolio(request):    
    assert isinstance(request, HttpRequest)
    context={"portfolios":Portfolio.objects.filter(is_home=True, is_active=True),
             #"categories":Category.objects.all()}
             }
    return render(
        request,
        'app/portfolio.html', context
        #{
        #    'title':'portfolio',
        #    'message':'TEMCO Mühendislik',
        #    'year':datetime.now().year,
        #}
    )

def portfoliodetail(request, slug):
    assert isinstance(request, HttpRequest)
    context={"portfolios":Portfolio.objects.get(slug=slug) }  
    return render(request, 'app/portfoliodetail.html', context)

def hizmetlerimiz(request):
    assert isinstance(request, HttpRequest)
    context={'hizmetler':Hizmetler.objects.filter(is_active=True, is_home=True),
             'title':'hizmetlerimiz',
            'message':'TEMCO Mühendislik',
            'year':datetime.now().year,}
    return render(
        request,
        'app/hizmetlerimiz.html',context
       
    )

def kurumsal(request):
    context={'kurumsals':Kurumsal.objects.all()}
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/kurumsal.html', context
        #{
        #    'title':'kurumsal',
        #    'message':'TEMCO Mühendislik',
        #    'year':datetime.now().year,
        #}
    )

def blog(request, tag_slug=None):
    assert isinstance(request, HttpRequest) 
    tag_slug=None
    if tag_slug:
        tag=get_object_or_404(TaggableManager, slug=tag_slug)
        posts = blog.filter(tags__in=[tag])

    context={"blogs":Blog.objects.filter(is_home=True, is_active=True),
             "categories":Category.objects.all()}  
    return render(request, 'app/blog.html', context, {'tag':tag})

def blog(request):
    assert isinstance(request, HttpRequest)
   
    query = request.GET.get("q")
    if query:
        posts=Blog.objects.filter(Q (title__icontains=query) | Q (tags__name__icontains=query)).distinct()
        
    postss = Blog.objects.filter(is_home=True, is_active=True)   
    paginator = Paginator(postss,4)     
    page_number = request.GET.get('blog')
    page_obj = paginator.get_page(page_number)

    context={"blogs":Blog.objects.filter(is_home=True, is_active=True),
             "last_four":Blog.objects.filter(is_home=True, is_active=True).order_by('-id')[:4],
             "categories":Category.objects.all(),
             "page_obj":page_obj}  
    return render(request, 'app/blog.html', context)

def blogdetails(request, slug):
    assert isinstance(request, HttpRequest)
    query = request.GET.get("q")
    if query:
        posts=Blog.objects.filter(Q (title__icontains=query) | Q (tags__name__icontains=query)).distinct()

    context={
        "blogs":Blog.objects.get(slug=slug),
        "categories":Category.objects.all(),
        "last_four":Blog.objects.filter(is_home=True, is_active=True).order_by('-id')[:4]
        }
    
    return render(
        request,                 
        'app/blogdetails.html',context
       
    ) 

def blogs_by_category(request, slug):
    
    postss = Category.objects.get(slug=slug).blog_set.filter(is_active=True)    
    paginator = Paginator(postss,3)     
    page_number = request.GET.get('blog')
    page_obj = paginator.get_page(page_number)

    context={"blogs":postss,
            #"blogs":Blog.objects.filter(is_active=True, category__slug=slug),
             "categories":Category.objects.all(),
             "selected_category":slug,
             "page_obj":page_obj
             }  
    return render(request, 'app/blog.html', context)

