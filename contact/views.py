from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def ContactPage(request):
    """
    View for contact page
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact/contact.html')

    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact/contact.html', context)
