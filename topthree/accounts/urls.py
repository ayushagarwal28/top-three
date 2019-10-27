from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_user, name = 'login'),
    path('logout/', views.logout_user, name = 'logout'),
    path('register/', views.register_user, name = 'register'),
    path('profile/<str:username>', views.details_user, name = 'details'),
    path('delete/poll/<int:poll_id>', views.delete_poll, name ='delete_poll'),
]
