from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('portfoliodetail/<slug:slug>', views.portfoliodetail, name='portfoliodetail'),
    path('hizmetlerimiz', views.hizmetlerimiz, name='hizmetlerimiz'),    
    path('kurumsal', views.kurumsal, name='kurumsal'),
    path('blogdetails/<slug:slug>', views.blogdetails, name='blogdetails'),
    path('tag/<slug:tag_slug>', views.blog, name='tag_blog'),
    path("category/<slug:slug>", views.blogs_by_category, name="blogs_by_category"),    
    path('login/',
         LoginView.as_view
         (             
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)