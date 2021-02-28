from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class Orders(models.Model):
    flataddress=models.CharField(max_length=50,default="Not provided")
    apartmentaddress=models.CharField(max_length=50)
    buyername=models.CharField(max_length=50,default="not given")
    quantity=models.CharField(max_length=10,default="1")
    phonenumber=models.CharField(max_length=20,default="not given")
    productname=models.CharField(max_length=32)
    dealername=models.CharField(max_length=32)
    orderstatus=models.CharField(max_length=32,default="In Process")
class EarnCredits(models.Model):
    STATUS_CHOICES=(('draft','Draft'),('published','Published'))
    completed=models.BooleanField(default=False)
    title=models.CharField(max_length=256)
    slug=models.SlugField(max_length=264,unique_for_date='publish')
    author=models.CharField(max_length=256)
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    image=models.ImageField(upload_to='images',blank=True)
class Post(models.Model):
    AVAIL_CHOICES=(('all','All'),("skillbattleartist","Skillbattle artist"),("gabblecastpodcaster","Gabblecast podcaster"),("skillbattleambassador","Skillbattle ambassador"),("gabblecast_ambassador","Gabblecast ambassador"),("skillbattleabroadartist","Skillbattle abroad artist"),("gabblecastabroadpodcaster","Gabblecast abroad podcaster"))
    STATUS_CHOICES=(('draft','Draft'),('published','Published'))
    title=models.CharField(max_length=256)
    slug=models.SlugField(max_length=264,unique_for_date='publish')
    marketer=models.CharField(max_length=256)
    marketer_phonenumber=models.CharField(max_length=10)
    product_details=models.TextField()
    product_link=models.CharField(max_length=256,default="no link")
    video_link = models.CharField(max_length=256,default="you")
    sample_price=models.IntegerField()
    product_price=models.IntegerField()
    available_region=models.CharField(max_length=120)
    available_in=models.CharField(max_length=25,choices=AVAIL_CHOICES,default='all')
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    image=models.ImageField(upload_to='images')
    class Meta:
        ordering=('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail',args=[self.publish.year,self.publish.strftime('%m'),self.publish.strftime('%d'),self.slug])
