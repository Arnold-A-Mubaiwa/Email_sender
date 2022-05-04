from django.shortcuts import render
from .forms import Sendmail
from django.core.mail import send_mail
from .models import Subscriber
from .models import Subscription, Email
from django.http import HttpResponse
import io
import csv
from django.contrib import messages
from sms import send_sms
# Create your views here.

def sendauto(request):
    if request.method == 'POST':
        form = Sendmail(request.POST)
        if form.is_valid():
            send_with = form.cleaned_data['send']
            subscription = form.cleaned_data['subscription']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            cc_myself = form.cleaned_data['cc_myself']
            
            recipients = []
            recipients_phone = []
            
            for r_list in Subscriber.objects.filter(subscription = subscription):
                # recipients.append(r_list.email)
                recipients = [r_list.email]
                recipients_phone = [r_list.email.phone]
                    
            if send_with == 'sms':
                send_sms(
                    message, '+2642681132', [recipients_phone], fail_silently=False
                )
                return HttpResponse("Thank you!")
            else:
                sender='arnold@gmail.com'
                if cc_myself:
                    recipients.append(sender)
                message += subscription    
                send_mail(subject, message,sender, recipients)
                msg ='Thanks, Message sent!'
                form = Sendmail()
                return render(request, 'mail/index.html',{'form':form,'msg':msg})
    else:
        form = Sendmail()
        msg = 'Message not sent.'
        return render(request, 'mail/index.html',{'form':form})
        
def upload_csv(request):
    
    template= "contact_upload.html"
    prompt = {
        'order': "order should be name, email, number"
    }
    
    if request.method == 'GET':
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.errors(request,"File is not a csv")
        return render(request, template)
        
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar='|'):
        created = Email.objects.update_or_create(
            Username = column[0],
            email = column[1]
        )
    
    context = {
         "msg":"Thanks,Well done"
    }
    return render(request, template,context)