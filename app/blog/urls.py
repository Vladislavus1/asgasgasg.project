from django.urls import path
from .views import render_main_page, send_message, render_message_page

urlpatterns = [
    path('', render_main_page, name='render_main_page'),
    path('send_message', send_message, name='send_message'),
    path('messages', render_message_page, name='messages'),
]