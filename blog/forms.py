from .models import Post, Comment, Contact
from django import forms


class PostForm(forms.ModelForm):
    body = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={'rows': '3',
                   'placeholder': 'Write your post...'}
        ))


    class Meta:
        model = Post
        fields = ['body']


class CommentForm(forms.ModelForm):
    body = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={
                'rows':'3',
                'placeholder': 'Write your comment..'
            }
        )
    )
    

    class Meta:
        model = Comment
        fields = ('comment',)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message',)