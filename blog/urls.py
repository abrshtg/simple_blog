from django.urls import path,include
from .import views
from rest_framework import routers
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView
# )


# router = routers.DefaultRouter()
# router.register("all", views.WildLifeView)

urlpatterns = [
    # path('',include(router.urls)),
    path('',views.url_list, name='list'),
    path('all/',views.home, name='home'),
    # path('user/', views.users, name='user'),
    path('wild/post', views.post, name='post'),
    path('<int:n>', views.detail, name='find_by_id'),
    path('<str:title>', views.detail, name='detail'),
    # # path('register/', views.register, name='register'),
    # # path('login/', views.login, name='login'),
    # # path('logout/', views.logout, name='logout'),
    path('wild/delete/<str:title>', views.wildupdate),
    path('wild/update/<str:title>', views.wildupdate),
    # # path('currency/', views.currency, name='currency')
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]