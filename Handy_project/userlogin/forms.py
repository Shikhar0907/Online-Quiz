from django import forms
from .models import User_Signup,quiz_questions
from django.core.exceptions import ValidationError
CHOICES = (('Handy','Handy'),('Home Cleaning','Home Cleaning'))

class userdetails(forms.ModelForm):
    services = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    class Meta():
        model = User_Signup
        fields = ['name','email','services']

    def clean_name(self):
        username = self.cleaned_data.get('name')
        if username.istitle() != True:
            raise forms.ValidationError("Please enter the first letter as capital in Username")
        return(username)

    def clean_choices(self):
        choices = self.cleaned_data.get('services')
        if choices is None:
            raise forms.ValidationError("Please select the services")

class questions(forms.ModelForm):
    class Meta():
        model = quiz_questions
        fields = '__all__'

