from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import requests

import gspread
from oauth2client.service_account import ServiceAccountCredentials

keywords = input('Search keyword: ')

driver = webdriver.Chrome('./chromedriver')
driver.get('https://news.google.com/?hl=ko&gl=KR&ceid=KR%3Ako')
driver.implicitly_wait(3)

search = driver.find_element_by_xpath('//*[@id="gb"]/div[2]/div[2]/div/form/div[1]/div/div/div/div/div[1]/input[2]')
search.send_keys(keywords)
search.send_keys(Keys.ENTER)
driver.implicitly_wait(30)

url = driver.current_url
resp = requests.get(url)
soup = bs(resp.text, 'lxml')

titles = []
links = []

for link in soup.select('h3 >a'):
    href = 'https://news.google.com' + link.get('href')[1:]
    title = link.string
    titles.append(title)
    links.append(href)

data = {'title': titles, 'link': links}
data_frame = pd.DataFrame(data, columns=['title', 'link'])




###google sheet
scope = ['https://spreadsheets.google.com/feeds']
json_file_name = '/Users/mac_yk/OneDrive/@coding/hanbit_crawling/hbprojectyk-5c5f3b0ec892.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
gc = gspread.authorize(credentials)
spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1gqL7yS5xS-ER2Nyp9hxA9_63GOM8I0Qy_8x0Xh7eUmA/edit?usp=sharing'

#문서 및 시트 불러오기
doc = gc.open_by_url(spreadsheet_url)
worksheet = doc.worksheet('a')

##쓰기
#셀 업데이트
worksheet.append_row([data_frame]) 