from django import forms
from .models import UserProfile
from datetime import date


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'dob']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'})  # HTML5 date input
        }

    def clean_dob(self):
        dob = self.cleaned_data.get('dob')
        if dob is None:
            raise forms.ValidationError("This field is required.")
        
        today = date.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

        if age < 18:
            raise forms.ValidationError("You must be at least 18 years old to submit this form.")
        
        return dob

