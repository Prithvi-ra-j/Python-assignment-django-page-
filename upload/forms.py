from django import forms
class uplooad(forms.Form):
    file=forms.FileField(label='Upload your Excel/CSV file')