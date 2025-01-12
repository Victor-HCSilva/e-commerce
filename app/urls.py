from django.urls import path
from . import views
from . import views_for_main

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login_, name='login'),
    path('logout/', views.logout_, name='logout'),
    path('main/<int:id>/', views.main, name='main'),
]