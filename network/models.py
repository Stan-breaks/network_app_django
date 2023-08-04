from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Sum

class User(AbstractUser):
    pass

class Post(models.Model):
    user= models.ForeignKey("User", on_delete=models.CASCADE, related_name="emails")
    text=models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def serialize(self):
        try:
            likes_count=Like.objects.filter(post=self).all().count()
        except Like.DoesNotExist:
            likes_count=0
        return{
            "id":self.id,
            "user":self.user.username,
            "text":self.text,
            "likes":likes_count,
            "timestamp":self.timestamp.strftime("%b %d %Y, %I:%M %p"),
        }
    
class Like(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE, related_name="liked_post")
    user=models.ManyToManyField(User,blank=False,related_name='likedUser')
    liked=models.BooleanField(default=False)

class Follower(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, related_name="followed_user")
    followers=models.ManyToManyField(User,blank=False,related_name='following_user')

