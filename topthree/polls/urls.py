from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('list/', views.poll_list, name = 'list'),
    path('add/', views.add_poll, name = 'add'),
    path('details/<int:poll_id>', views.poll_detail, name = 'details'),
    path('details/<int:poll_id>/vote', views.poll_vote, name = 'vote'),
]
