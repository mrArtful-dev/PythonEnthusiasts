import requests
from bs4 import BeautifulSoup as BS
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

rub_eur_link = 'https://www.google.com/search?q=rub+to+eur&oq=rub+t&aqs=chrome.0.0i433i512j69i57j0i512l8.5836j1j7&sourceid=chrome&ie=UTF-8'

r = requests.get(rub_eur_link, headers=headers)
soup = BS(r.content, 'html.parser')
match = soup.find_all('span', class_='DFlfde SwHCTb')
# exchange_rate = float(match.text.replace(',', '.'))
exchange_rate = float(match['data-value'])
# print(match)
user_sum = float(input('Please enter amount in EUR: '))
print(user_sum * exchange_rate, 'RUB')

user_sum = float(input('Please enter amount in RUB:'))
print(user_sum / exchange_rate, 'EUR')
