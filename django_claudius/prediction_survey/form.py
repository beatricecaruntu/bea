from django import forms
from django.forms import ModelForm
from django_claudius.models import Case

class CaseForm(ModelForm):
    class Meta:
        model = Case
        exclude = "__all__"

    def clean_age(self):
        age = self.cleaned_data['age']

        # Age should be between 1-120
        if age < 1 or age > 120:
            raise forms.ValidationError("Invalid Age")

        return age

    def clean(self):
        cleaned_data = super().clean()

        # Any custom multi-parameter cleaning goes here

        return cleaned_data

class Page1Form(CaseForm):
    class Meta(CaseForm.Meta):
        fields = ('name','age',)

class Page2Form(CaseForm):
    class Meta(CaseForm.Meta):
        fields = ('hospital_bill',)




