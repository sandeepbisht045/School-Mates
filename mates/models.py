from django.db import models
from django.utils import timezone
import math

# Create your models here.
class Users(models.Model):
    email=models.EmailField()
    
    name=models.CharField(max_length=20,default="aa")
    password=models.CharField(max_length=30)
    
    def __str__(self):
        return self.name





class Mates(models.Model):
    name=models.CharField(max_length=100)
    about=models.CharField(max_length=1000)
    photo=models.ImageField(upload_to="",default="defaultpic.png")
    added_by=models.ForeignKey(Users,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name    
    
    
class User_comments(models.Model):
    user=models.ForeignKey(Users,on_delete=models.CASCADE)
    comment=models.CharField(max_length=200)
    time=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-time',]
    
    def __str__(self):
        return str(self.user)
    # _____________________________________________________________________________________________________________
    
    
    def whenpublished(self):
        now = timezone.now()
        
        diff= now - self.time

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds
            
            if seconds == 1:
                return str(seconds) +  "second ago"
            
            else:
                return str(seconds) + " seconds ago"

            

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + " minute ago"
            
            else:
                return str(minutes) + " minutes ago"



        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)

            if hours == 1:
                return str(hours) + " hour ago"

            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
        
            if days == 1:
                return str(days) + " day ago"

            else:
                return str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            

            if months == 1:
                return str(months) + " month ago"

            else:
                return str(months) + " months ago"


        if diff.days >= 365:
            years= math.floor(diff.days/365)

            if years == 1:
                return str(years) + " year ago"

            else:
                return str(years) + " years ago"
 
    
    

    
    
