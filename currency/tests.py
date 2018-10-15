import json
from decimal import Decimal
from unittest import mock

from django.test import TestCase, RequestFactory
from django.urls import reverse

from currency.mocks import CONVERT_SUCCESS_BODY, CONVERT_SUCCESS_RESPONSE, CONVERT_SUCCESS_FAIL, \
    ADD_CURRENCY_SUCCESS_RESPONSE, OPEN_EXCHANGE_RATES_MOCK_1, \
    ADD_CURRENCY_BODY, ADD_CURRENCY_FAIL_RESPONSE, OPEN_EXCHANGE_RATES_MOCK_2
from currency.services import CurrencyService
from currency.tasks import update_exchange_rates
from currency.views import ConvertCurrencyView, AddCurrencyView
from utils.adapters.open_exchange_rate import open_exchange_rate_adapter


class TestConvertCurrencyView(TestCase):
    fixtures = ['currency/fixtures/fixtures.json']

    def setUp(self):
        self.factory = RequestFactory()
        self.url = reverse('convert-currency')

    def test_convert_success(self):
        req = self.factory.post(self.url)
        req.JSON = CONVERT_SUCCESS_BODY
        response = ConvertCurrencyView.as_view()(req)
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content, CONVERT_SUCCESS_RESPONSE)

    def test_convert_fail(self):
        req = self.factory.post(self.url)
        req.JSON = CONVERT_SUCCESS_FAIL
        response = ConvertCurrencyView.as_view()(req)
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 400)


class TestAddCurrencyView(TestCase):
    fixtures = ['currency/fixtures/fixtures.json']

    def setUp(self):
        self.factory = RequestFactory()
        self.url = reverse('add-currency')

    @mock.patch.object(open_exchange_rate_adapter, 'get_exchange_rate', return_value=OPEN_EXCHANGE_RATES_MOCK_1)
    @mock.patch.object(open_exchange_rate_adapter, 'check_currency', return_value=True)
    def test_add_currency_success(self, check_currency, get_exchange_rate):
        req = self.factory.post(self.url)
        req.JSON = ADD_CURRENCY_BODY
        response = AddCurrencyView.as_view()(req)
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content, ADD_CURRENCY_SUCCESS_RESPONSE)

    @mock.patch.object(open_exchange_rate_adapter, 'get_exchange_rate', return_value=OPEN_EXCHANGE_RATES_MOCK_1)
    @mock.patch.object(open_exchange_rate_adapter, 'check_currency', return_value=False)
    def test_add_currency_fail(self, check_currency, get_exchange_rate):
        req = self.factory.post(self.url)
        req.JSON = ADD_CURRENCY_BODY
        response = ConvertCurrencyView.as_view()(req)
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(content, ADD_CURRENCY_FAIL_RESPONSE)


class TestCurrencyService(TestCase):
    fixtures = ['currency/fixtures/fixtures.json']

    def test_convert_currency_RUB_TO_EUR(self):
        converted_amount = CurrencyService.convert_currency('RUB', 'EUR', 500)
        self.assertEqual(converted_amount, Decimal('6.5803'))

    def test_convert_currency_USD_TO_EUR(self):
        converted_amount = CurrencyService.convert_currency('USD', 'EUR', 100)
        self.assertEqual(converted_amount, Decimal('86.4000'))


class TestUpdateExchangeRates(TestCase):
    fixtures = ['currency/fixtures/fixtures.json']

    @mock.patch.object(open_exchange_rate_adapter, 'get_exchange_rate', return_value=OPEN_EXCHANGE_RATES_MOCK_2)
    def test_update_exchange_rates(self, mock):
        update_exchange_rates()
        for type, rate in OPEN_EXCHANGE_RATES_MOCK_2.items():
            exchange_rate = CurrencyService.get_exchange_rate(type)
            self.assertEqual(exchange_rate, round(Decimal(rate), 3))
