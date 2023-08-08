import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator

from .models import User,Post,Like,Account


def index(request):
    return render(request, "network/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
            account=Account.objects.create(user=user)
            account.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

@csrf_exempt
def post(request):
    if request.method=='POST':
        if request.user.is_authenticated:
            data= json.loads(request.body)
            text=data.get("text")
            if not text:
              return JsonResponse({"error":"Post is empty"},status=400)
            post=Post(user=request.user,text=text)
            post.save()
            return JsonResponse({"message":"Post was successful"},status=200)
        else:
            return JsonResponse({'error':'you need to login'})
    else:
        posts=Post.objects.all()
        posts=posts.order_by("-timestamp").all()
        return JsonResponse([post.serialize() for post in posts],safe=False)

@csrf_exempt
@login_required
def like(request,post_id):
    if request.method!='POST':
        return JsonResponse({'ERROR':'fuckery detected'})
    post=Post.objects.get(pk=post_id)
    user=request.user
    try:
        likes=Like.objects.get(post=post,user=request.user)
    except Like.DoesNotExist:
        likes=None
    if not likes:
        likes=Like.objects.create(post=post,liked=True)
        likes.user.add(user)
        return JsonResponse({'message':'Liked'})
    else:
        likes.user.remove(user)
        likes.delete()
        return JsonResponse({'message':'Unliked'})

def account(request):
   if request.method!='POST':
       accounts=Account.objects.all()
       return JsonResponse([account.serialize() for account in accounts],safe=False)
    
@csrf_exempt      
@login_required     
def follow(request,username):
    user=request.user
    followeduser=User.objects.get(username=username)
    useraccount=Account.objects.get(user=user)
    followedaccount=Account.objects.get(user=followeduser)
    if user.username in followedaccount.follower.values_list('username',flat=True):
        useraccount.following.remove(followeduser)
        followedaccount.follower.remove(user)
        return JsonResponse({'message':'Unfollow successful'})
    useraccount.following.add(followeduser)
    followedaccount.follower.add(user)
    return JsonResponse({'message':'Follow successful'})

@login_required
def profile(request,username):
    user = get_object_or_404(User, username=username)
    account = get_object_or_404(Account, user=user)
    posts=Post.objects.filter(user=user).order_by("-timestamp").all()
    serialized_posts=[post.serialize() for post in posts]
    return render(request,"network/profile.html",{
        "username":username,
        "followers":account.follower.count(),
        "following":account.following.count(),
        "posts":serialized_posts,
        "isuser":username==request.user.username,
        "isfollow":request.user.username in account.follower.values_list('username',flat=True)
    })

@login_required
def following(request):
    user=request.user
    account=Account.objects.get(user=user)
    posts=[]
    for accountuser in account.following.all():
        user_posts = Post.objects.filter(user=accountuser)
        posts.extend(user_posts)
    sorted_posts = sorted(posts, key=lambda post: post.timestamp, reverse=True)
    serialized_posts=[post.serialize() for post in sorted_posts]
    return render(request,'network/following.html',{
        "posts":serialized_posts,
    })









