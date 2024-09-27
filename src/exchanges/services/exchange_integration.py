from decimal import Decimal
from time import sleep

from faker.generator import random


class ExchangeService:

    @classmethod
    def buy_from_exchange(cls, *, crypto_name: str, amount: Decimal):
        """ This is a placeholder for the actual HTTP request to an international exchange"""
        print(f"Buying {amount} of {crypto_name} from international exchange")
        # In a real implementation, you would make an HTTP request here
        # response = requests.post('https://international-exchange-api.com/buy', json={
        #     'cryptocurrency': cryptocurrency,
        #     'amount': amount
        # })
        # return response.json() or order_id
        sleep(5)  # Placeholder for the time it takes to make the request
        return random.randint(1, 1000)  # Placeholder for order_id
