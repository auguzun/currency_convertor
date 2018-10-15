from django.contrib import admin
from django.urls import path
from django.views.decorators import csrf

from currency.views import ConvertCurrencyView, AddCurrencyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('convert_currency/',
         csrf.csrf_exempt(ConvertCurrencyView.as_view()),
         name='convert-currency'),
    path('add_currency/', csrf.csrf_exempt(AddCurrencyView.as_view()),
         name='add-currency')

]
