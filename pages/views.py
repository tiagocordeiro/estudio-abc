from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm


def home(request):
    return render(request, 'pages/index.html')


def about(request):
    return render(request, 'pages/quem_somos.html')


def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            from_name = form.cleaned_data['from_name']
            from_email = form.cleaned_data['from_email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message,
                          from_name + ' <' + from_email + '>',
                          ['tiago@mulhergorila.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "pages/contact.html", {'form': form})


def success(request):
    return render(request, 'pages/obrigado.html')
