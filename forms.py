from django import forms


class Contactform(forms.Form):
    name=forms.CharField(label="Name",max_length=100)
    email=forms.EmailField(label="Email",max_length=100)
    message=forms.CharField(label="Message",max_length=100)
    
