from django.contrib import messages
from .models import Message


def create_message(form, request):
    message = form.save(commit=False)
    message.author = request.user
    message.publish()
    messages.success(request, message='Message sent!')


def get_all_messages():
    return Message.objects.all()