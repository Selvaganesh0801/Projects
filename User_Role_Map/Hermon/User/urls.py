from django.contrib import admin
from django.urls import path

from .views import *

from User import views


urlpatterns = [
    path('get/', views.UserDetail),
    path('create/', UserPost.as_view()),
    path('get/<int:id>', UserInfo.as_view()),
    path('update/', userUpdate.as_view()),
    path('delete/<int:id>', userDelete.as_view()),
    path('role_get/', RoleDetails.as_view()),
    path('role_create/', RolePost.as_view()),
    path('role_get/<int:id>', RoleInfo.as_view()),
    path('role_update/', RoleUpdate.as_view()),
    path('role_delete/<int:id>', RoleDelete.as_view()),

]



