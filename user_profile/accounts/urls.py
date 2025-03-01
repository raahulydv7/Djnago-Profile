
from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage_view,name='home'),
    path('register/', views.register_view,name='register'),
    path('login/', views.login_view,name='login'),
    path('logout/', views.logout_view,name='logout'),
]