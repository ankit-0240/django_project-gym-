from django.urls import path
from fit import views

urlpatterns = [
    path('', views.Home),
    path('signup',views.signup),
    path('login',views.handlelogin),
    path('logout',views.handleLogout),
    path('contact',views.con),
    path('join',views.enroll),
    path('workout',views.work),
    path('diet',views.diet),
    path('profile',views.profile),
    path('gallery',views.gallery),
    path('attendance',views.attendance),
    
]
