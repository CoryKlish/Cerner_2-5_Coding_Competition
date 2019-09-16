import requests
from bs4 import BeautifulSoup as Soup

#cerner_2^5_2019

'''
Retrieves current Cerner Stock Price and prints after running
'''

response = requests.get('https://www.marketwatch.com/investing/stock/cern')

if response.status_code == 200:
    soup = Soup(response.text, features = 'html.parser')
    print(soup.findAll('bg-quote', {'class': 'value'})[0].text)
else:
    print('Failure getting stock price...try again')
