from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass
class Post(models.Model):
    user=user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="emails")
    text=models.TextField(blank=True)
    likes=models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    def serialize(self):
        return{
            "self":self.id,
            "user":self.user,
            "likes":self.likes,
            "timestamp":self.timestamp
        }

class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE, related_name="post")
    user=models.ManyToManyField(User,blank=False,related_name='commentUser')
    comment=models.CharField(max_length=200)
