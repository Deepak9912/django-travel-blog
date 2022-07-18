from django.shortcuts import render
from .forms import ContactForm
from django.http import HttpResponse


# Create your views here.
def ContactPage(request):
    """
    View for contact page
    """
    print('reached function')

    form = ContactForm
    context = {'form': form}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        print('posted')
        if form.is_valid():
            form.save()
            return render(request, 'contact.html', context)
            
    return render(request, 'contact.html', context)
