import requests
from bs4 import BeautifulSoup
import re


def user_choice():
        user_input = input('Пожалуйста, выберите:\n1) Конвертация биткоина к евро\n2) Конвертация евро к биткоину\n-->')

        if user_input == '1':
            amount = float(input('Введите сумму:\n-->'))
            result_1 = amount * do_convert()
            result_string = '{result:.2f} евро'
            print(result_string.format(result=result_1))
            user_choice()
        elif user_input == '2':
            amount = float(input('Введите сумму:\n-->'))
            result_1 = amount / do_convert()
            result_string = '{result:.2f} биткоин'
            print(result_string.format(result=result_1))
            user_choice()
        else:
            print('Не входит в диапазон')
            user_choice()

def do_convert():
    BTC_EUR = 'https://www.google.com/search?q=btc+eur&sca_esv=557735838&sxsrf=AB5stBgNm20461pOky2BxiW2PMvZIRKLPg%3A1692262685653&ei=HeHdZLW_J4CvwPAPlI-XoAs&ved=0ahUKEwj1wfrhqeOAAxWAFxAIHZTHBbQQ4dUDCA8&uact=5&oq=btc+eur&gs_lp=Egxnd3Mtd2l6LXNlcnAiB2J0YyBldXIyDBAjGIoFGCcYRhiCAjIGEAAYBxgeMggQABgHGB4YCjIGEAAYBxgeMggQABgHGB4YDzIGEAAYBxgeMgYQABgHGB4yBhAAGAcYHjIGEAAYBxgeMgYQABgHGB5I2RNQpwtY3hBwAXgBkAEAmAF-oAHZAqoBAzAuM7gBA8gBAPgBAcICChAAGEcY1gQYsAPCAgoQABiKBRiwAxhDwgIHECMYsAIYJ8ICCRAAGAcYHhjxBMICBxAjGIoFGCfiAwQYACBBiAYBkAYK&sclient=gws-wiz-serp'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
    full_page = requests.get(BTC_EUR, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", class_="pclqee")
    result = convert[0].text.replace('\xa0', '')
    result_1 = result.replace(',', '.')

    return float(result_1)


user_choice()
