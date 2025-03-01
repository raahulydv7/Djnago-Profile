
from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage_view,name='home'),
    path('register/', views.register_view,name='register'),
]