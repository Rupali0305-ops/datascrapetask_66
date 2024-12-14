from playwright.sync_api import sync_playwright
from selectolax.parser import HTMLParser

def gethtml(websiteurl, showbrowser=True, screenshotname = ''):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless= not showbrowser)
        page = browser.new_page()
        page.goto(url=websiteurl)

        page.wait_for_load_state('networkidle')
        page.wait_for_load_state('domcontentloaded')
        page.wait_for_timeout(1000)


        if screenshotname != '':
            page.screenshot(full_page=True, path=f'./{screenshotname}.png')

        pagehtml = page.inner_html('body')

        pagedata = HTMLParser(pagehtml)

        return pagedata 
    