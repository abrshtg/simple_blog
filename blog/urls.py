from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name='home'),
    path('<int:wildlife_id>', views.detail, name='detail'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('post', views.post, name='post'),
    path('currency', views.currency, name='currency')
]