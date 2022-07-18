from django.shortcuts import render
from .forms import ContactForm
from django.http import HttpResponse


# Create your views here.
def ContactPage(request):
    """
    View for contact page
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Thank you for contacting us</h1>")
            

    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact.html', context)
