from django.urls import path
from . import views


urlpatterns = [
    path('', views.UserView.as_view(), name='home'),
    path('post_create', views.PostCreateView.as_view(), name='post_create'),
]