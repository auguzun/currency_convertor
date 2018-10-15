class CurrencyException(Exception):
    status_code = 500
    message = 'ServiceError'
    reason = 'currencyException'

    def __init__(self, message=None, errors=None):
        if message:
            self.message = message
        if errors is None:
            self.errors = [{'reason': self.reason}]
        else:
            self.errors = errors


class CurrencyDoesNotExist(CurrencyException):
    status_code = 404
    message = 'Currency not found.'
    reason = 'currencyNotFound'


class OpenExchangeRateError(CurrencyException):
    message = 'Open Exchange Rate api returned an error'
    reason = 'openExchangeRateError'
