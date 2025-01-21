from django import forms
class MyForm(forms.Form):
    id = forms.IntegerField(label='enter id')
    name = forms.CharField(max_length=20)
    image = forms.ImageField()
    price = forms.IntegerField(label='enter price')
    
    