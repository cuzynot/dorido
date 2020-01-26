from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup
import time
from selenium import webdriver
    
url = "https://www.canadiantire.ca/en/search-results.html?q=screwdriver"

options = webdriver.ChromeOptions()
options.add_argument('headless')
browser = webdriver.Chrome("C:/Users/yilis/Downloads/chromedriver_win32/chromedriver.exe", chrome_options=options)

def scrape(url):
    browser.get(url)
    time.sleep(1)
    print("len", len(browser.page_source))
    print(browser.page_source[0])
    curStore = url[url.index(".") + 1:]
    curStore = curStore[:curStore.index(".")]
    print(curStore)

    # initialize lists
    allNames = []
    allPrices = []
    allStores = []
    allRatings = []

    # parse html
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    
    if (curStore == "nofrills" or curStore == "loblaws" or curStore == "fortinos"):
        names = soup.findAll("span", {"class":"product-name__item--name"})
        prices = soup.findAll("span", {"class":"price__value selling-price-list__item__price selling-price-list__item__price--now-price__value"})

        for item in names:
            allNames.append(item.text)

        for item in prices:
            allPrices.append(item.text)

    elif (curStore == "metro"):        
        names = soup.findAll("div", {"class":"pt-title"})
        prices = soup.findAll("div", {"class":"pi--main-price"})
        
        for item in names:
            allNames.append(item.text)
            
        for item in prices:
            allPrices.append(item["data-main-price"])

    elif (curStore == "ebgames"):
        names = soup.findAll("div", {"class":"singleProdInfo"})
        prices = soup.findAll("a", {"class":"megaButton cartAddNoRadio"})

        for item in prices:
            allPrices.append(item.span.b.text)
            
        for i in range(len(prices)):
            allNames.append(names[i].h3.a.text)

    elif (curStore == "toysrus"):
        names = soup.findAll("div", {"class":"b-product_tile-caption"})
        prices = soup.findAll("span", {"class":"b-price-value js-sales-price-value"})

        for item in names:
            allNames.append(item.h2.a.text[2:-2])

        for item in prices:
            allPrices.append(item.text[2:-2])

    elif (curStore == "mastermindtoys"):
        names = soup.findAll("span", {"itemprop":"name"})
        prices = soup.findAll("span", {"itemprop":"price"})
    
        for item in names:
            allNames.append(item.text)

        for item in prices:
            allPrices.append(item.text)

    elif (curStore == "canadiantire"):
        names = soup.findAll("h3", {"class":"product-tile-srp__title grid--grid-view__item specialCss"})
        prices = soup.findAll("section", {"class":"product-tile__price"})

        for item in names:
            allNames.append(item.text)

        for item in prices:
            allPrices.append(item.text.replace(" ", "").replace("\n", ""))

    
    #############################
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
