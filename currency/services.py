from currency.repository import CurrencyRepository


class CurrencyService:

    @classmethod
    def get_all_types(cls):
        return CurrencyRepository.get_all_types()

    @classmethod
    def get_exchange_rate(cls, currency_type):
        return CurrencyRepository.get_exchange_rate(currency_type)

    @classmethod
    def convert_currency(cls, currency_from, currency_to, amount):
        """

        :param currency_from: type of currency to convert from
        :param currency_to: type of currency to convert to
        :param amount: amount to convert
        :return: converted amount
        """
        currency_from_rate = cls.get_exchange_rate(currency_from)
        currency_to_rate = cls.get_exchange_rate(currency_to)
        converted_amount = amount * (currency_to_rate/currency_from_rate)
        return round(converted_amount, 4)

    @classmethod
    def update_exchange_rate(cls, currency_type, exchange_rate):
        CurrencyRepository.update_exchange_rate(currency_type, exchange_rate)

    @classmethod
    def add_currency(cls, currency):
        CurrencyRepository.add_currency(currency)
