from django import forms
from .models import Customer, ShippingAddress


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'company_name',
            'country'
        ]
        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),
            "email": forms.EmailInput(attrs={
                "class": "form-control"
            }),
            "phone_number": forms.TextInput(attrs={
                "class": "form-control"
            }),
            "company_name": forms.TextInput(attrs={
                "class": "form-control"
            }),
            "country": forms.TextInput(attrs={
                "class": "form-control"
            })
        }


class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = [
            "address_1",
            "address_2",
            "city",
            "state",
        ]
        widgets = {
            "address1": forms.TextInput(attrs={
                    "class": "form-control"
                }),
            "address2": forms.TextInput(attrs={
                "class": "form-control"
            }),
            "city": forms.TextInput(attrs={
                "class": "form-control"
            }),
            "state": forms.TextInput(attrs={
                "class": "form-control"
            })
        }

