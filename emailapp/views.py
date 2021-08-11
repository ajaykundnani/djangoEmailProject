from django.shortcuts import render,HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def index(request):
    if request.method == 'POST':
        msg = request.POST['message']
        send_mail('Subject', 
        msg , 
        settings.EMAIL_HOST_USER , 
        ['ajaykundnani2529@gmail.com'] , 
        fail_silently=False)
    return render(request,'index.html')
