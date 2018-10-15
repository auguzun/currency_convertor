import json

from django.http import JsonResponse
from django.views import View

from currency.forms import ConvertCurrencyValidationForm, AddCurrencyValidationForm
from currency.services import CurrencyService
from currency.tasks import update_exchange_rates


class ConvertCurrencyView(View):
    def post(self, request):
        data_form = ConvertCurrencyValidationForm(request.JSON)
        if data_form.is_valid():
            cleaned_data = data_form.clean()
            amount = CurrencyService.convert_currency(cleaned_data['currencyFrom'], cleaned_data['currencyTo'],
                                                      cleaned_data['amount']
                                                      )
            return JsonResponse(status=200, data={'success': True, 'amount': amount})
        else:
            return JsonResponse(
                status=400, data={'success': False,
                                  'errors': [(k, v[0]) for k, v in data_form.errors.items()]}
            )


class AddCurrencyView(View):
    def post(self, request):
        data_form = AddCurrencyValidationForm(request.JSON)
        if data_form.is_valid():
            new_currency = data_form.clean()['currency']
            CurrencyService.add_currency(new_currency)
            # Updating exchange rates for all currencies to fill new currency rate
            update_exchange_rates()
            return JsonResponse(status=200, data={'success': True, 'message': 'Currency has been added'})
        else:
            return JsonResponse(
                status=400, data={'success': False,
                                  'errors': [(k, v[0]) for k, v in data_form.errors.items()]}
            )
