from django import forms
from .models import Complain
from entities.models import Entity
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
        if promoter.person.id == demmanded_person.id:
            # the first argument of the add_error method is set to None
            # so the error will be added to the non_field_errors attribute

            # if any other validation is necesary in the future, all errors will be
            # raised at once and all the mistakes mada by the user will be seen together.
            self.add_error(None, 'La persona no puede ser igual al promovente')
        else:
            return cleaned_data