from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(max_length=100, label='Your name')
    
class ContactUs(forms.Form):
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)