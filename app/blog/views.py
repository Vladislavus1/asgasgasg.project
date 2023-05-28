from django.shortcuts import render, redirect
import requests
from .forms import *
from .controllers import *
from django.contrib import messages
# Create your views here.


def render_main_page(request):
    form = Form()
    return render(request, 'main.html', {'form': form})


def render_message_page(request):
    messages = get_all_messages()
    return render(request, 'messages.html', {'messages': messages})


def send_message(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            create_message(form, request)
        else:
            messages.error(request, 'There was an error while adding question, check your data and try again.')
        return redirect('/')

