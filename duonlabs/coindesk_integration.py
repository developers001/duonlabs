import requests
import json

class CoinDeskIntegration:
    def __init__(self):
        self.api_url = 'https://api.coindesk.com/v1/bpi'

    def fetch_current_price(self):
        response = requests.get(f'{self.api_url}/currentprice.json')
        return json.loads(response.text)

    def fetch_historical_data(self, start_date, end_date):
        response = requests.get(f'{self.api_url}/historical/close.json?start={start_date}&end={end_date}')
        return json.loads(response.text)

# Example usage:
# coindesk = CoinDeskIntegration()
# print(coindesk.fetch_current_price())
# print(coindesk.fetch_historical_data('2026-03-01', '2026-03-26'))