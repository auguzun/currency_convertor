from __future__ import absolute_import, unicode_literals

import decimal
import logging

from celery import task

from currency.services import CurrencyService
from utils.adapters.open_exchange_rate import open_exchange_rate_adapter


@task()
def update_exchange_rates():
    """
    Task for updating exchange rate. Runs periodically
    """
    try:
        logging.info('starting to update exchange rates')
        all_types = CurrencyService.get_all_types()
        exchange_rates = open_exchange_rate_adapter.get_exchange_rate(all_types)
        for currency_type, exchange_rate in exchange_rates.items():
            CurrencyService.update_exchange_rate(currency_type, decimal.Decimal(exchange_rate))
        logging.info(f'Exchange rates updated for {[*exchange_rates]}')
    except Exception as e:
        logging.exception(f'Failed to update exchange rates, error {e}')
