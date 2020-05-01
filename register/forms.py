from django import forms

class ExampleForm(forms.Form):
   name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
   email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
   address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
   country = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))