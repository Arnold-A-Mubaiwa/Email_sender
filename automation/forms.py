from django import forms
from .models import Subscription

sub_choice = [tuple([sub.id,sub]) for sub in Subscription.objects.all()]
contact_choice = [
    ('sms','sms'),
    ('email','email')
]
class Sendmail(forms.Form):
    send = forms.ChoiceField( choices=contact_choice)
    subscription =  forms.CharField(widget=forms.Select(choices=sub_choice))
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)
    cc_myself = forms.BooleanField(required=False)
    # bb = forms.ChoiceField(choices=sub_choices)