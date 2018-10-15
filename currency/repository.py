from django.core.exceptions import ObjectDoesNotExist
from django.utils.timezone import now

from currency.models import Currency
from utils.exceptions import CurrencyDoesNotExist


class CurrencyRepository:

    @classmethod
    def get_currency_object(cls, currency_type):
        try:
            return Currency.objects.get(type=currency_type)
        except ObjectDoesNotExist:
            raise CurrencyDoesNotExist

    @classmethod
    def get_all_types(cls):
        return Currency.objects.values_list('type', flat=True).distinct()

    @classmethod
    def get_exchange_rate(cls, currency_type):
        return cls.get_currency_object(currency_type).exchange_rate

    @classmethod
    def update_exchange_rate(cls, currency_type, exchange_rate):
        Currency.objects.filter(type=currency_type).update(exchange_rate=exchange_rate, updated=now())

    @classmethod
    def add_currency(cls, currency):
        Currency.objects.get_or_create(type=currency)


