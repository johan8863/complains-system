from django import forms
from .models import Complain


class ComplainForm(forms.ModelForm):
    class Meta:
        model = Complain
        fields = '__all__'

        # The date field must be sent configured and formatted in a widget so the date picker can read it.
        # This configuration is only relative to the way the date is entered, the type of the input must be 
        # specified in the template in the input tag or using the widget_tweaks package.
        widgets = {
            'reception_date': forms.DateInput(
                format=('%Y-%m-%d'),
                ),
        }