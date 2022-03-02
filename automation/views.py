from django.shortcuts import render
from .forms import Sendmail
from django.core.mail import send_mail
from .models import Subscriber
from .models import Subscription
from django.http import HttpResponse
# Create your views here.

def sendauto(request):
    if request.method == 'POST':
        form = Sendmail(request.POST)
        if form.is_valid():
            subscription = form.cleaned_data['subscription']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            cc_myself = form.cleaned_data['cc_myself']
            
            sender='arnold@gmail.com'
            recipants = []
            for r_list in Subscriber.objects.filter(subscription = subscription):
                recipants.append(r_list.email)
                
            if cc_myself:
                recipants.append(sender)
            message += subscription    
            send_mail(subject, message,sender, recipants)
            return HttpResponse('Thanks')
    else:
        form = Sendmail()
        return render(request, 'mail/index.html',{'form':form})
    