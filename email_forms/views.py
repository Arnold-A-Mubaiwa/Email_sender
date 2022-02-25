from django.shortcuts import render
from django.http import HttpResponse
from .forms import NameForm, ContactUs
from django.core.mail import send_mail
# Create your views here.
def index(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            
            return HttpResponse('Thanks')
    else:
        form = NameForm()
            
    return render(request, 'forms/index.html', {'form':form})

def contact_us(request):
    if request.method=='POST':
        form = ContactUs(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']
            
            recipients = ['arnoldmubaiwa99@gmail.com']
            
            if cc_myself :
                recipients.append(sender)
            
            send_mail(subject,message,sender, recipients)
            return HttpResponse('Thanks') 
        
    else:
        form = ContactUs()
        return render (request, 'forms/contact.html',{'form':form})