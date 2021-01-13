from django import forms

class CodeForm(forms.Form):
    # thecode = forms.TextAreaField(label='Your name', max_length=100)
    thecode = forms.CharField(widget=forms.Textarea)