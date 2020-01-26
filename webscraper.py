from bs4 import BeautifulSoup
import time
from selenium import webdriver
from pymongo import MongoClient
        
def scrape(browser, collection, itemName, url):
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
    
    # parse html
    soup = BeautifulSoup(browser.page_source, 'html.parser')

    html = browser.page_source

##    while 1:
##        if itemName not in html:
##            break
##
##        html = html[html.index(itemName):]
##
##        if "<" not in html and '"' not in html:
##            break
##
##        ind = int(2**30)
##        if "<" in html:
##            ind = html.index("<")
##        if '"' in html and html.index('"') < ind:
##            ind = html.index('"')
##                  
##        name = html[0:ind]
##        html = html[ind:]

##        print(name)
##        if len(name) >= len(itemName) and len(name) < 40:
##            print(name)

    
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

    # add all members to mongo db
    for i in range(min(len(allNames), len(allPrices))):
        newItem = {
            "item": itemName,
            "description": allNames[i],
            "price": allPrices[i],
            "store": curStore
        }

        collection.insert_one(newItem)



def scrapeAll(urls):
    # selenium
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    browser = webdriver.Chrome("C:/Users/yilis/Downloads/chromedriver_win32/chromedriver.exe", chrome_options=options)

    # mongodb
    client = MongoClient("mongodb://yililiu:yililiu@dhcluster-shard-00-00-zicz8.gcp.mongodb.net:27017,dhcluster-shard-00-01-zicz8.gcp.mongodb.net:27017,dhcluster-shard-00-02-zicz8.gcp.mongodb.net:27017/test?ssl=true&replicaSet=DHCluster-shard-0&authSource=admin&retryWrites=true&w=majority")
    db = client.get_database("deltahacks")
    collection = db.dorido

    # scrape all items
    itemName = urls[0]
    for i in range(1, len(urls)):
        scrape(browser, collection, itemName, urls[i])

    print(collection.count_documents({}))


#scrape(url)

scrapeAll(["dorito", "https://www.nofrills.ca/search?search-bar=dorito"])


