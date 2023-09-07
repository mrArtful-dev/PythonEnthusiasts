import time

from selenium import webdriver
import pandas as pd

url = 'https://www.youtube.com/@visitestoniaofficial/videos'
pd.set_option('display.max_columns', 5)

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

driver.find_element('xpath', '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/form[1]/div/div/button/span').click()

videos = driver.find_elements('id', 'content')

video_lst = []
for vid in videos:
    try:
        res = {
            'title': vid.find_element('xpath', './/*[@id="video-title"]').text,
            'length': vid.find_element('xpath', './/*[@id="text"]').text,
            'link': vid.find_element('xpath', './/*[@id="video-title-link"]').get_attribute('href')
        }
        video_lst.append(res)
    except Exception as err:
        print('err')

data = pd.DataFrame(video_lst)
print(data)