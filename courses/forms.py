from django import forms

class ContactForm(forms.Form):
    your_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)