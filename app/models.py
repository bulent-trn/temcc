from ast import Not
from email.policy import default
from operator import not_
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField 
from taggit.managers import TaggableManager
from django.utils import timezone
from embed_video.fields import EmbedVideoField


class TagDict(models.Model):
    id=models.BigAutoField(primary_key=True)
    tag = models.CharField(max_length=100)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.tag

class Category(models.Model):
    id=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=150)
    slug=models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        self.slug=slugify(self.name)
        super().save(*args, **kwargs)

class Blog(models.Model):
    id=models.BigAutoField(primary_key=True)
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to="blogs")
    video2=EmbedVideoField(null=True, blank=True)
    description=RichTextField()
    is_active=models.BooleanField(default=False)
    is_home=models.BooleanField(default=False)
    slug=models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)
    categories=models.ManyToManyField(Category, blank=True)
    tags=TaggableManager(blank=True)
    date_published = models.DateTimeField(null=True, blank=True, default=timezone.now)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        self.slug=slugify(self.title)
        if not self.video2:
            self.video2 = None        
        super(Blog, self).save(*args, **kwargs)

        for tag in self.tags.all():
            tag_dict,_ = TagDict.objects.get_or_create(tag=str(tag))
            tag_dict.count += 1
            tag_dict.save()


class Product(models.Model):
    id=models.BigAutoField(primary_key=True)
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to="products", null=False)
    image2=models.ImageField(upload_to="products", null=True)
    image3=models.ImageField(upload_to="products", null=True)
    description=RichTextField()
    is_active=models.BooleanField(default=False)
    is_home=models.BooleanField(default=False)
    slug=models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)
    date_published = models.DateTimeField(null=True, blank=True, default=timezone.now)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):        
        self.slug=slugify(self.title)
        super().save(*args, **kwargs)
 



class Portfolio(models.Model):
    id=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=200)
    image=models.ImageField(upload_to="portfolios", null=False)
    image2=models.ImageField(upload_to="portfolios", null=True)
    image3=models.ImageField(upload_to="portfolios", null=True)
    description=RichTextField()   
    is_active=models.BooleanField(default=False)
    is_home=models.BooleanField(default=False)
    slug=models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)
    project_date = models.DateTimeField(null=True, blank=True, default=timezone.now)
    project_link=models.CharField(max_length=200, null=True)

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        self.slug=slugify(self.name)
        super().save(*args, **kwargs)

class Hizmetler(models.Model):
    id=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=200)
    image=models.ImageField(upload_to="hizletler", null=False)
    description=RichTextField()   
    is_active=models.BooleanField(default=False)
    is_home=models.BooleanField(default=False)
    slug=models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        self.slug=slugify(self.name)
        super().save(*args, **kwargs)


class Kurumsal(models.Model):
    id=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=200)
    hakkinda=RichTextField()
    faaliyetlerimiz=RichTextField()
    neredeyiz=RichTextField()
    iletisim_yollari=RichTextField()

    def __str__(self):
        return f"{self.name}"
