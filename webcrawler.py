from webscraper import scrapeAll

def crawl(item):
    links = [item]

    links.append("https://www.nofrills.ca/search?search-bar=" + item)
    links.append("https://www.loblaws.ca/search?search-bar=" + item)
    links.append("https://www.fortinos.ca/search?search-bar=" + item)
    links.append("https://www.metro.ca/en/search?filter=" + item + "&freeText=true")
    links.append("https://www.ebgames.ca/SearchResult/QuickSearch?q=" + item)
    links.append("https://www.toysrus.ca/en/search?q=" + item + "&search-button=&lang=en_CA")
    links.append("https://www.mastermindtoys.com/search/" + item + ".aspx")
    links.append("https://www.canadiantire.ca/en/search-results.html?q=" + item)

    links.append("https://www.dollarama.com/en-CA/Search?keywords="+item)
    links.append("https://www.costco.ca/CatalogSearch?dept=All&keyword="+item)
    links.append("https://www.bestbuy.ca/en-ca/search?search="+item)
    links.append("https://www.ikea.com/ca/en/search/products/?q="+item)
    #links.append("https://www.ashleyhomestore.ca/search?type=product&q="+item)
    links.append("https://www.staples.ca/search?query="+item)
    #links.append("https://www.rona.ca/webapp/wcs/stores/servlet/RonaAjaxCatalogSearchView?storeId=10151&catalogId=10051&langId=-1&searchKey=RonaEN&content=&keywords="+item)
    #links.append("https://www.officedepot.com/a/browse/"+item+"/N=5+4520&viewAllSkus=true/?hijack=pens&type=Search")
    links.append("https://www.partycity.com/ca/search?q="+item+"&lang=en_CA")
    #links.append("https://www.wholesaleclub.ca/search/1580036973438/page/~item/"+item+"/~sort/recommended/~selected/true")    
    links.append("https://www.valumart.ca/search?search-bar="+item)
    #links.append("https://www.londondrugs.com/search/?q="+item+"&lang=default")

    return(scrapeAll(links))

crawl("doritos")
    
