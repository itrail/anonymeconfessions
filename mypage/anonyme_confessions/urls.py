from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:articles_id>/', views.articles_id, name="articles_id"),
    path('new/', views.add_article, name='add_article'),
    path('login_view/', views.login_view, name='login_view'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register_view, name='register_view'),
]
