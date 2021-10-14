from django.urls import path
from . import views


urlpatterns = [
    path('', UserView.as_view(), name='home'),
]