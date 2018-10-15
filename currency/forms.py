from django import forms

from currency.services import CurrencyService
from utils.adapters.open_exchange_rate import open_exchange_rate_adapter


class ConvertCurrencyValidationForm(forms.Form):
    amount = forms.DecimalField(decimal_places=3)
    currencyFrom = forms.CharField()
    currencyTo = forms.CharField()

    def clean(self):
        cleaned_data = super().clean()
        currency_from = cleaned_data.get("currencyFrom")
        currency_to = cleaned_data.get("currencyTo")
        all_types = CurrencyService.get_all_types()
        if currency_from not in all_types:
            self.add_error('currencyFrom', 'This currency in not supported, please add it')
        if currency_to not in all_types:
            self.add_error('currencyTo', 'This currency in not supported, please add it')
        return cleaned_data


class AddCurrencyValidationForm(forms.Form):
    currency = forms.CharField()

    def clean_currency(self):
        currency = self.cleaned_data.get("currency")
        currency_exists = open_exchange_rate_adapter.check_currency(currency)
        if not currency_exists:
            raise forms.ValidationError(f"Currency {currency} doesn't exist")
        return currency