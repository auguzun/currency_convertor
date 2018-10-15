import logging

import requests

from config import settings
from utils.exceptions import OpenExchangeRateError


class OpenExchangeRateAdapter:

    def __init__(self, url, api_id):
        self.url = url
        self.api_id = api_id

    def get_exchange_rate(self, currency_types=None):
        """
        Gets exchange rates for specific types of currencies
        :param currency_types: types of requested currencies
        :return: dict of rates
        """
        try:
            params = {'app_id': self.api_id}
            if currency_types:
                params['symbols'] = ','.join(currency_types)
            response = requests.get(url=f'{self.url}/latest.json', params=params)
            if response.ok:
                json_body = response.json()
                json_data = json_body['rates']
                return json_data
            else:
                logging.error(f'OpenExchangeRate returned an error {response}')
                raise OpenExchangeRateError
        except Exception as e:
            logging.exception(f'Exception during request to OpenExchangeRate {e}')
            raise OpenExchangeRateError

    def check_currency(self, currency_type):
        """
            Checks if currency exists
        :param currency_type
        :return: True/False
        """
        try:
            response = requests.get(url=f'{self.url}/currencies.json')
            if response.ok:
                json_body = response.json()
                return currency_type in json_body.keys()
            else:
                logging.error(f'OpenExchangeRate returned an error {response}')
                raise OpenExchangeRateError
        except Exception as e:
            logging.exception(f'Exception during request to OpenExchangeRate {e}')
            raise OpenExchangeRateError


open_exchange_rate_adapter = OpenExchangeRateAdapter(settings.OPEN_EXCHANGE_RATE_URL,
                                                     settings.OPEN_EXCHANGE_RATE_API_ID)
