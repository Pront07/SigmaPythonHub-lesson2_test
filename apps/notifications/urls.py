
from django.urls import path
from . import views

app_name = 'notifications'

urlpatterns = [
    path('show/', views.notifications, name='show_notifications'),
]