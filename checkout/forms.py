from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Orderfields = ('full_name', 'email', 'phone_number',
                               'street_address1', 'street_address2',
                               'town_or_city', 'postcode', 'country',
                               'county')

    def __init__(sefl, *args, **kwargs):
        """
            add placeholders and classes, remove auto-generated 
            labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'email',
            'phone_number': 'phone number',
            'country': 'country',
            'postcode': 'postcode',
            'town_or_city': 'Town Or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholder[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False