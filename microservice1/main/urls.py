from django.urls import path
from main import views

urlpatterns = [
    path('send_message', views.send_message_view),
]
