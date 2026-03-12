from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.test,name="test"),
    path('create/', views.tweet_create, name='tweet_create'),
]
