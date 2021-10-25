from django.urls import path
from . import views


urlpatterns = [
    path('', views.UserView.as_view(), name='home'),
    path('post_create', views.PostCreateView.as_view(), name='post_create'),
    path('thanks/', views.ThanksView.as_view(), name="thanks"),
    path('userpage/<int:pk>/', views.UserView.as_view(), name="userpage")
]