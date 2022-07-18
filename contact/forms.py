from django.forms import ModelForm
from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']

    
    def __init__(self, *args, **kwargs):
        """ 
        Add placeholders and classes and remove autogenerated labels
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Please enter your full name',
            'email': 'Please enter your email address',
            'message': 'Write your query here..',
        }

        self.fields['email'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder