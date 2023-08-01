from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Sum
from django.utils import timezone

class User(AbstractUser):
    pass

class Post(models.Model):
    user= models.ForeignKey("User", on_delete=models.CASCADE, related_name="emails")
    text=models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def serialize(self):
        likes_count=Like.objects.filter(post=self).aggregate(Sum('amount'))['amount__sum'] or 0
        comments=Comment.objects.filter(post=self) 
        comments_list=[
            {
                "id":comment.id,
                "user":comment.user.username,
                "commenttext":comment.commenttext,
                "timestamp":comment.timestamp.strftime("%b %d %Y, %I:%M %p")
            }
            for comment in comments
        ]
        
        return{
            "id":self.id,
            "user":self.user.username,
            "text":self.text,
            "likes":likes_count,
            "timestamp":self.timestamp.strftime("%b %d %Y, %I:%M %p"),
            "comments":comments_list
        }
    
class Like(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE, related_name="liked_post")
    user=models.ManyToManyField(User,blank=False,related_name='likedUser')
    amount=models.IntegerField()

class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE, related_name="comment_post")
    user=models.ManyToManyField(User,blank=False,related_name='commentUser')
    commenttext=models.CharField(max_length=200,blank=True)
    timestamp=models.DateTimeField(default=timezone.now)
