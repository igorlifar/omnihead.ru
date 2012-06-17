from django import forms

class ContactForm(forms.Form):

    author = forms.CharField(max_length=500)
    email = forms.EmailField(max_length=100)
    message = forms.CharField(widget=forms.Textarea(), max_length=5000)