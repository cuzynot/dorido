from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup
import time
from selenium import webdriver
    
url = "https://www.loblaws.ca/search?search-bar=dorito"

options = webdriver.ChromeOptions()
options.add_argument('headless')
browser = webdriver.Chrome("C:/Users/yilis/Downloads/chromedriver_win32/chromedriver.exe", chrome_options=options)

def scrape(url):
    browser.get(url)
    time.sleep(1)
    print("len", len(browser.page_source))
    curStore = url[12:]
    curStore = curStore[:curStore.index(".")]
    print(curStore)

    # initialize lists
    names = []
    prices = []
    stores = []
    
    allNames = []
    allPrices = []
    allStores = []

    # parse html
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    
    if (curStore == "nofrills" or curStore == "loblaws"):
        names = soup.findAll("span", {"class":"product-name__item--name"})
        prices = soup.findAll("span", {"class":"price__value selling-price-list__item__price selling-price-list__item__price--now-price__value"})
##        names = browser.find_elements_by_class_name("product-name__item--name")
    elif (curStore == "walmart"):
        names = soup.findAll("h2")
        prices = soup.findAll("div", {"possibleRangedCurrencyText: { data: price, simpleFormatting: simpleFormatting } "})
    elif (curStore == "loblaws"):        
        names = soup.findAll("span", {"class":"product-name__item product-name__item--name"})
        prices = soup.findAll("span", {"class":"price__value selling-price-list__item__price selling-price-list__item__price--now-price__value"})
    
    # add to lists
    for item in names:
        if (item.text != ""):
            allNames.append(item.text)

    for item in prices:
        if (item.text != ""):
            allPrices.append(item.text)

    for i in range(len(allNames)):
        allStores.append(curStore)

    # print lists
    print(len(allNames))
    print(allNames)
    print(allPrices)
    print(allStores)


def scrapeAll(url):
    for u in url:
        scrape(url)


scrape(url)
