from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_Api),
    path('user/', views.get_userdata),
    path('register/', views.register_Api),
    path('logout/', views.LogoutView.as_view(), name='knox_logout'),
    # path('logout/', views.LogoutView),

]