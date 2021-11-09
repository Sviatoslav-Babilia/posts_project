from django.urls import path, include
import debug_toolbar
from django.conf import settings

from . import views


urlpatterns = [
    path('', views.UserView.as_view(), name='home'),
    path('post_create', views.PostCreateView.as_view(), name='post_create'),
    path('thanks/', views.ThanksView.as_view(), name="thanks"),
    path('userpage/<int:pk>/', views.UserView.as_view(), name="userpage"),
    path('allposts/', views.AllPostsView.as_view(), name='allposts'),
    path('__debug__/', include(debug_toolbar.urls)),
    
    
]