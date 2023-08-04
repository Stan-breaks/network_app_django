
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("post",views.post,name="post"),
    path("account",views.account,name="account"),
    path("account/<str:username>",views.get_account,name='getaccount'),
    path("like/<int:post_id>",views.like,name='like'),
    path("profile/<int:user_id>",views.profile,name='profile')
]
