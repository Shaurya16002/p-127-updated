import csv
import time
from selenium import webdriver
from bs4 import BeautifulSoup

url = 'https://exoplanets.nasa.gov/exoplanet-catalog/'
browser = webdriver.Chrome('chromedriver')
browser.get(url)
time.sleep(10)
def scrape():
    headers = ['name','lightyears_from_earth','Planet_mass','stellar_magnitude','Discovery_date']

    planetData = []

    for i in range(0,507):
        soup = BeautifulSoup(browser.page_source,'html.parser')
    
        for s in soup.find_all('ul',attrs={'class','exoplanet'}):
            li = s.find_all('li')
            tempList = []

            for index,l in enumerate(li):
                if index==0:
                    tempList.append(l.find_all("a")[0].contents[0])

                else:
                    try:
                        tempList.append(l.contents[0])

                    except:
                        tempList.append('')
        
            planetData.append(tempList)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    
    with open('c127.csv','w')as file:
        fileWriter = csv.writer(file)
        fileWriter.writerow(headers)
        fileWriter .writerows(planetData)
    
scrape()