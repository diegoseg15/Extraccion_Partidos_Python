from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time

path = r'C:\Users\User\Documents\Programas\Ejecutables\chromedriver\chromedriver.exe'
options = webdriver.ChromeOptions()
# options.binary_location = r'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe'
# options.binary_location = r'C:\Users\User\AppData\Local\Programs\Opera developer\opera.exe'
service = Service(path)
# driver = webdriver.Chrome(service=service, options=options)
driver = webdriver.Chrome(service=service)


def obtener_data_faltante(year):
    web = f'https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup'

    driver.get(web)

    matches = driver.find_elements(
        by='xpath', value='//td[@align="right"]/.. | //td[@style="text-align:right;"]/..')

    home = []
    score = []
    away = []

    for match in matches:
        home.append(match.find_element(by='xpath', value='./td[1]').text)
        score.append(match.find_element(by='xpath', value='./td[2]').text)
        away.append(match.find_element(by='xpath', value='./td[1]').text)

    dict_football = {'home': home, 'score': score, 'away': away}
    df_football = pd.DataFrame(dict_football)
    df_football['year'] = year
    time.sleep(2)

    return df_football


years = [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974,
         1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014,
         2018, 2022]

fifa = [obtener_data_faltante(year) for year in years]
driver.quit()
df_fifa = pd.concat(fifa, ignore_index=True)
df_fifa.to_csv('fifa_worldcup_missing_data.csv', index=False)
