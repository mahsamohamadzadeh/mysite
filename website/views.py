from django.shortcuts import render
from .forms import ContactForm, NewsLetterForm
from django.http import HttpResponseRedirect
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request, 'website/index.html')


def about(request):
    return render(request, 'website/about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'your ticket seved successfully', 'success')
        else:
            messages.warning(request, 'your ticket didnt seve ', 'warning')

    form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})


def newsletter(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
