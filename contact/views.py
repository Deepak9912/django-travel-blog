from django.shortcuts import render
# from .forms import ContactForm
from .models import Contact
from django.http import HttpResponse

# Create your views here.
def ContactPage(request):
    """
    View for contact page
    """
    if request.method == 'POST':
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact.name=name
        contact.email=email
        contact.message=message
        contact.save()
        return HttpResponse("<h1>Thank you for your email!</h1>")

            # return render(request, 'success.html')

    return render(request, 'contact.html')
