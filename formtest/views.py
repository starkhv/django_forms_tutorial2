from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import NameForm, ContactForm


def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = NameForm()

    return render(request, 'formtest/index.html', {'form': form})


def thanks(request):
    return render(request, 'formtest/thanks.html', {})


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['info@example.com']
            if cc_myself:
                recipients.append(sender)
            #send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/thanks/')
    else:
        form = ContactForm()

    return render(request, 'formtest/contact.html', {'form': form})
