from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class ContactForm(forms.ModelForm):
    name = models.CharField(label='name' max_length=100)
    email = models.EmailField(label='email')
    message = models.TextField(label='message')