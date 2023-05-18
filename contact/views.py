from django.shortcuts import render
# import contact
from .models import Contact
# import messages
from django.contrib import messages
# Create your views here.

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
        messages.success(request, 'تم ارسال الرساله بنجاح')
    return render(request,'contact.html')

def contact_ar(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
        messages.success(request, 'تم ارسال الرساله بنجاح')
    return render(request,'contact-ar.html')