from django.shortcuts import render
from .forms import Contact_form


def contact(request):

    if str(request.method) == 'POST':

        form = Contact_form(request.POST)

        if form.is_valid():
            form.send_email()
            form = Contact_form()
        else:
            pass

    else:
        form = Contact_form()
    
    context = {
        "form": form
    }

    template_name = 'sendmail/contact.html'
    
    return render(request, template_name, context)
