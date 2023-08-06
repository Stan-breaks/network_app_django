from django.test import TestCase,Client
from .models import Post,Account,Like,User
from django.db.models import Max
# Create your tests here.

class SocialTestCase(TestCase):
    def setUp(self):
        #Create the users and their account
        self.user1=User.objects.create_user('peter','peter@example.com','123456')
        account1=Account.objects.create(user=self.user1)
        self.user2=User.objects.create_user('trevis','trevis@example.com','123456')
        account2=Account.objects.create(user=self.user2)

        #users follow each other accounts
        account1.follower.set([self.user2])
        account1.following.set([self.user2])
        account2.follower.set([self.user1])
        account2.following.set([self.user1])

        # Assigning client role to user1 initially  
        self.client_user = self.user1 

        #create the post
        post1=Post.objects.create(user=self.user1,text='Hello world!')
        post2=Post.objects.create(user=self.user2,text='Hello world!')

        #create likes
        Like.objects.create(post=post1,user=self.user1)
        Like.objects.create(post=post1,user=self.user2)
        Like.objects.create(post=post2,user=self.user1)
        Like.objects.create(post=post2,user=self.user2)
    def test_post(self):
        posts=Post.objects.all()
        self.assertEqual(posts.count(),2)
    def text_account(self):
        accounts=Account.objects.all()
        self.assertEqual(accounts.count(),2)
    def test_likes_in_post(self):
        user=User.objects.get(username='peter')
        post=Post.objects.get(user=user)
        likes=Like.objects.filter(post=post).all()
        self.assertEqual(likes.count(),2)
    def test_index(self):
        c=Client()
        response=c.get('')
        self.assertEqual(response.status_code,200)
    def test_following_page(self):
        response=self.client.get('/Following')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.context['posts'].count(),1)
    def test_profile_page(self):
        response=self.client.get('/profile/peter')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.context['posts'].count(),1)
    def test_follower(self):
        account=Account.objects.first()
        self.assertEqual(account.follower.count(),1)
    def test_following(self):
        account=Account.objects.first()
        self.assertEqual(account.following.count(),1)



