import pandas as pd
from playwright.sync_api import sync_playwright
from selectolax.parser import HTMLParser
from utils.extractHtml import gethtml

flipurl = "https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=laptop%7CLaptops&requestId=1ba12086-0177-4c14-9c3b-0c95a1c53806%27%20nse50%20=%20%27https://www.nseindia.com/market-data/live-equity-market?symbol=NIFTY%2050%27%20page.goto(flipUrl)"
flipheader = {
    "user-agent": 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36',
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en-US,en;q=0.9,hi-IN;q=0.8,hi;q=0.7,mr-IN;q=0.6,mr;q=0.5,az-AZ;q=0.4,az;q=0.3",
    "cache-control": "max-age=0",
    "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "sec-ch-ua-arch": "\"\"",
    "sec-ch-ua-full-version": "\"131.0.6778.109\"",
    "sec-ch-ua-full-version-list": "\"Google Chrome\";v=\"131.0.6778.109\", \"Chromium\";v=\"131.0.6778.109\", \"Not_A Brand\";v=\"24.0.0.0\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-model": "\"Nexus 5\"",
    "sec-ch-ua-platform": "\"Android\"",
    "sec-ch-ua-platform-version": "\"6.0\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "cookie": "T=TI173399394896100131777700445805726894534475162694205128009245184179; at=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImQ2Yjk5NDViLWZmYTEtNGQ5ZC1iZDQyLTFkN2RmZTU4ZGNmYSJ9.eyJleHAiOjE3MzU3MjE5NDgsImlhdCI6MTczMzk5Mzk0OCwiaXNzIjoia2V2bGFyIiwianRpIjoiNzY0NjUwMTEtMzI0OS00ZGMzLWIzY2YtMzhkMWE5NWRmY2YyIiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNzMzOTkzOTQ4OTYxMDAxMzE3Nzc3MDA0NDU4MDU3MjY4OTQ1MzQ0NzUxNjI2OTQyMDUxMjgwMDkyNDUxODQxNzkiLCJrZXZJZCI6IlZJMUM1MkM5MkQ3QzBDNEI3NEI3MzJEOTlENjU5MThBOTkiLCJ0SWQiOiJtYXBpIiwidnMiOiJMTyIsInoiOiJDSCIsIm0iOnRydWUsImdlbiI6NH0.RKncRk9BKT172FFUBGXlOSPfb3COlXIwOrQzGNcjwNc; rt=null; K-ACTION=null; ud=2.VogYwlUWqZC3mok_5Tvo2stTYjZu5u2qDbEYJRpeUrEiIztHA4giwD8hAU652G1fRModCoaWXDgXvHElraL3Ew52qTfbEu9Yk5Q1UVtjioP1QzbjLJNScgJ_AD36WgYGVrvvBrKzi6XfaAc4wDq8IA; qH=312f91285e048e09; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C20070%7CMCMID%7C78759362256239712971588060037109393182%7CMCAAMLH-1734598632%7C12%7CMCAAMB-1734598632%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1734001033s%7CNONE%7CMCAID%7CNONE; S=d1t17XD8lRz8/TFZTGz8/Pz9EP7fCA/ErSAl6jcIICgvUbILooSeSxOh39W1mHdWaJEQXOLCZKO/hAmWso9/XYfU5yw==; vh=651; vw=366; dpr=2.0000000298023224; fonts-loaded=en_loaded; isH2EnabledBandwidth=false; h2NetworkBandwidth=9; gpv_pn=ProductList; gpv_pn_t=ProductList; vd=VI1C52C92D7C0C4B74B732D99D65918A99-1733993951514-2.1733997158.1733997091.153814848; Network-Type=4g; SN=VI1C52C92D7C0C4B74B732D99D65918A99.TOKEA01AEE2A65042EDB51846A337807AAD.1733997169843.LO"

  }
if __name__ == '__main__':
    
    flipdata = gethtml(websiteurl=flipurl, showbrowser=False, screenshotname='lp3')
    alldata =[]

    producttitles = [t.text() for t in flipdata.css('div[class="KzDLHZ"]')]

    productratings = [r.text() for r in flipdata.css('div[class="XQDdHH"]')]
    #print(productratings)

    productprice = [p.text() for p in flipdata.css('div[class="Nx9bqj _4b5DiR"]')]
    #print(productprice)

    flipdata = {
        'producttitles': producttitles,
        'productratings': productratings,
        'productprice': productprice
    }
    alldata.append(flipdata)
flipdata = pd.DataFrame(alldata)
flipdata.to_csv('flipdata.csv')

    

