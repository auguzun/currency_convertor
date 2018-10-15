CONVERT_SUCCESS_BODY = {
    "amount": 1200,
    "currencyFrom": "RUB",
    "currencyTo": "EUR"
}

CONVERT_SUCCESS_FAIL = {
    "amount": 1200,
    "currencyFrom": "EKR",
    "currencyTo": "EUR"
}

CONVERT_SUCCESS_RESPONSE = {"success": True, "amount": "15.7926"}

ADD_CURRENCY_BODY = {"currency": "TND"}
ADD_CURRENCY_SUCCESS_RESPONSE = {
    "success": True,
    "message": "Currency has been added"
}
ADD_CURRENCY_FAIL_RESPONSE = {'success': False, 'errors': [['amount', 'This field is required.'],
                                                           ['currencyFrom', 'This field is required.'],
                                                           ['currencyTo', 'This field is required.']]}

OPEN_EXCHANGE_CURRENCIES_MOCK = {"TND": "Tunisian Dinar"}
OPEN_EXCHANGE_RATES_MOCK_1 = {
    "CZK": 22.3034,
    "EUR": 0.863895,
    "PLN": 3.717,
    "RUB": 66.065,
    "TND": 2.825903,
    "USD": 1

}
OPEN_EXCHANGE_RATES_MOCK_2 = {
    "CZK": 11.11,
    "EUR": 22.22,
    "PLN": 33.33,
    "RUB": 44.44,
    "USD": 66.66

}

