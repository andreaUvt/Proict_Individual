from django import forms
from django.core import validators
from app.models import User
 

class NewUserForm(forms.ModelForm):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter you email again:')
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])
    

    def clean(self):
        all_clean_data=super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email'] 

        if email !=vmail:
            raise forms.ValidationError("Email-urile trebuie sa fie egale")
    class Meta:
    
        model = User
        fields = '__all__'
