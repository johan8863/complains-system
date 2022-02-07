from django import forms
from .models import Complain
from django.core.exceptions import ValidationError


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

    def clean(self):
        cleaned_data = super().clean()
        promoter = cleaned_data.get('promoter')
        demmanded_person = cleaned_data.get('demmanded_person')
        print(promoter)
        print(demmanded_person)
        if promoter.person.id == demmanded_person.id:
            raise ValidationError('El promovente y la persona demandada no pueden ser el mismo/a')
        else:
            return cleaned_data