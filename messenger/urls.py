from django.urls import path
from . import views

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('enviar/', views.send_message, name='send_message'),
]
