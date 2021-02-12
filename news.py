###해당 주제 뉴스기사 10개 crawling
##우선 검색
#필요한 모듈
# $ pip install bs4
# $ pip install selenium
# $ pip install requests
# $ pip install pandas
# $ pip install openpyxl
# $ pip install lxml


from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import requests

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
data_frame.to_csv('./' + keywords + '.csv')
data_frame.to_excel('./' + keywords + '.xlsx')

print("Complete!")