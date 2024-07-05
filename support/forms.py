from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Ticket, Comment


class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'is_staff']


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['subject', 'description']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']