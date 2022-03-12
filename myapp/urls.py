from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('admin/', views.admin, name="admin"),
    path('service/', views.service, name="service"),
    path('service/<int:id>', views.view_service, name="view_service"),
    path('login/', views.user_login, name="login"),
    path('logout', views.user_logout, name="logout"),
]
