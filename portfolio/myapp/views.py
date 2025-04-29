from django.shortcuts import render
from django.http import HttpResponse
from .models import ContactUs1 




def resume(request):
    return render(request ,'resume_theme\\resume.html')



def about(request):
    return render(request, 'Manisha_theme\\about.html')



def home(request):
    return render(request, 'Manisha_theme\home.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = ContactUs1(name=name, phone=phone, email =email , message=message)
        contact.save()
        return HttpResponse('Your message has been sent')
    return render(request, 'contact.html')


def sports(request):
    return render(request ,'Manisha_theme\Sports.html')    

def academic(request):
    return render(request,'Manisha_theme\Academic.html')



