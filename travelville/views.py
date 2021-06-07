from django.shortcuts import render, redirect
from .models import Places
from django.core.mail import send_mail
from django.contrib import messages


def list_places(request):

    places = Places.objects.all()

    send = False

    # contact form
    if request.method == "POST":
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        text = request.POST.get('text', '')
        email = request.POST.get('email', '')

        subject = f"Message from: {name}, contact: {phone}"
        message = f"{text}"
        email = f"{email}"

        send_mail(subject, message, email, ['yeboahd24@gmail.com'])
        send = True
        # messages.add_message(request, messages.INFO, 'Send Successfully')
        return redirect('/')

    return render(request, 'index.html', {'places': places})
