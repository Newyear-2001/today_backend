from selenium import webdriver
from bs4 import BeautifulSoup
from html_table_parser import parser_functions

import time
import pandas as pd 

# xpath location
# //*[@id="mw-content-text"]/div[1]/table[6]
# //*[@id="mw-content-text"]/div[1]/table[6]/tbody
url = "https://en.wikipedia.org/wiki/List_of_cities_in_South_Korea"
driver = webdriver.Chrome('/home/imsky/문서/today_project/today_backend/weather/weather_infomation/chromedriver')
driver.get(url)

def html_source():
    # 목적지 elemect
    element = driver.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/table[6]')
    """
    # 방법 1 
    from selenium.webdriver.common.action_chains import ActionChains
    action = ActionChains(driver)
    action.move_to_element(element).perform()
    """
    # 목적지 element 까지 이동 (방법2)
    element.location_once_scrolled_into_view
    element.click()
    
    return driver.page_source

# making table
def bs4_source():
    html = html_source()
    soup = BeautifulSoup(html, 'lxml')
    time.sleep(1)
    data = soup.find("table", {"class": "wikitable sortable jquery-tablesorter"})
    
    # table 생성 
    table = parser_functions.make2d(data)
    make_table = pd.DataFrame(data=table[1:], columns=table[0])
    print(make_table)
    make_table.to_csv('city_table.csv', index=False, index_label=False)

        
bs4_source()