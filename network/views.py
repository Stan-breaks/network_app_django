import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .models import User,Post,Like


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
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

@csrf_exempt
@login_required
def post(request):
    if request.method=='POST':
        data= json.loads(request.body)
        text=data.get("text")
        if text=='':
            return JsonResponse({"error":"Post is empty"},status=400)
        post=Post(user=request.user,text=text)
        post.save()
        return JsonResponse({"message":"Post was successful"},status=200)
    else:
        posts=Post.objects.all()
        posts=posts.order_by("-timestamp").all()
        return JsonResponse([post.serialize() for post in posts],safe=False)

@csrf_exempt
@login_required
def like(request,post_id):   
    if request.method!='POST':
        return JsonResponse[{'ERROR':'fuckery detected'}]
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

@login_required
def profile(request,user_id):
    pass









