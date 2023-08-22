from django.urls import path

from . import views
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from django.views.generic import TemplateView
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("auctions/<int:bidid>", views.listingpage, name="listingpage"),
    path("watchlist/<str:username>", views.watchlistpage, name = "watchlistpage"),
    path("added", views.addwatchlist, name = "addwatchlist"),
    path("delete", views.deletewatchlist, name = "deletewatchlist"),
    path("bidlist", views.bid, name="bid"),
    path("comments", views.allcomments, name="allcomments"),
    path("win_ner", views.win_ner, name="win_ner"),
    path("winnings", views.winnings, name="winnings"),
    path("cat_list", views.cat_list, name="cat_list"),
    path("categories/<str:category_name>", views.cat, name="cat"),
    # forgot   
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='auctions/commons/password-reset/password_reset.html',
             subject_template_name='auctions/commons/password-reset/password_reset_subject.txt',
             email_template_name='auctions/commons/password-reset/password_reset_email.html',
             success_url='done/'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='auctions/commons/password-reset/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='auctions/commons/password-reset/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='auctions/commons/password-reset/password_reset_complete.html'
         ),
         name='password_reset_complete'),   
]

