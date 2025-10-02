import requests

data = requests.get('https://claraj.github.io/mock-bitcoin/currentprice.json').json()
print(data)

usd_rate = float(data['bpi']['USD']['rate'].replace(',', ''))

print()

print(f'The current Bitcoin price in USD is: {usd_rate}')

dollars = float(input('Enter an amount in USD: '))

bitcoins = round(dollars / usd_rate, 6)

print(f'{dollars:.2f} dollars in Bitcoin is: {bitcoins}')