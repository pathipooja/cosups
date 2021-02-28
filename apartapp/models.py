from django.db import models
from django.contrib.auth.models import User

# Create your models here.\
# class UserDetailManager(models.Manager):
#     def create_sb(self,firstname,lastname,username,email,collegename,year_class,Field_of_study,Hobbies):
#         userd=self.create(firstname=firstname,lastname=lastname,username=username,email=email,collegename=collegename,year_class=year_class,Field_of_study=Field_of_study,Hobbies=Hobbies)
#         return userd
class MarketerDetail(models.Model):
    AVAIL_CHOICES=(("skillbattleartist","Skillbattle artist"),("gabblecastpodcaster","Gabblecast podcaster"),("skillbattleambassador","Skillbattle ambassador"),("gabblecast_ambassador","Gabblecast ambassador"),("skillbattleabroadartist","Skillbattle abroad artist"),("gabblecastabroadpodcaster","Gabblecast abroad podcaster"))
    username=models.OneToOneField(User, on_delete=models.CASCADE)
    verified=models.BooleanField(default=False)
    credits = models.IntegerField(default=0)
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    phonenumber=models.IntegerField(default=18)
    email=models.EmailField(max_length=30)
    Type_of_community=models.CharField(max_length=25,choices=AVAIL_CHOICES)
    # no_of_blocks=models.IntegerField(default=0)
    # no_of_flats_or_houses=models.IntegerField()
    # currentbill=models.CharField(max_length=30)
    # adhaarnumber=models.IntegerField()
    # partner=models.CharField(max_length=30)
    instagramlink = models.CharField(max_length=40,default='')
    address=models.CharField(max_length=256,default="notgiven")
    pincode=models.IntegerField()
    state=models.CharField(max_length=30)
    district=models.CharField(max_length=30)
    sub_colony=models.CharField(max_length=30)
