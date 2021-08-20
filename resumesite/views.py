from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
# Create your views here.
def home(request):
    if request.method == 'POST':
        name = request.POST.get('full-name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message,
        }
        print(data)
        return HttpResponse ('Thank you for reaching out to Christian, we will be in touch soon')
    return render(request, 'home.html', {})