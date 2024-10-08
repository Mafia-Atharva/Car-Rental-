from django.http import JsonResponse
from django.shortcuts import render
from .models import Contact

# Create your views here.
def home(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        phone_number = request.POST.get('Phone Number')
        message = request.POST.get('Message')
        contact = Contact(name=name, email=email, phone_number=phone_number, message=message)
        contact.save()
        return JsonResponse({'status': 'success', 'message': 'Form submitted successfully! You will recieve an email from our executive soon. Thank you for using Trator!'})
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def gallery(request):
    return render(request, 'gallery.html')

def client(request):
    return render(request, 'client.html')

def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        phone_number = request.POST.get('Phone Number')
        message = request.POST.get('Message')
        contact = Contact(name=name, email=email, phone_number=phone_number, message=message)
        contact.save()
        return JsonResponse({'status': 'success', 'message': 'Form submitted successfully! You will recieve an email from our executive soon. Thank you for using Trator!'})
    return render(request, 'contact.html')

