from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('time/', views.curr_date_time),
    path('home/', views.home),
    path('polls/', include('polls.urls')),
]
