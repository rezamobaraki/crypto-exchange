from django.urls import include, path

app_name = 'exchanges'

urlpatterns = [
    path('crypto-currency/', include('exchanges.urls.crypto_currency', namespace='crypto_currency'),
         name='crypto_currency'),
]
