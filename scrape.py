import pandas as pd
from playwright.sync_api import sync_playwright, Page
import time
from bs4 import BeautifulSoup
from undetected_playwright import Tarnished
import webbrowser
from datetime import datetime
from pathlib import Path
 
def cache_screenshot(page: Page):
    _now = datetime.now().strftime("%Y-%m-%d")
    _suffix = f"-view-new-{datetime.now().strftime('%H%M%S')}"
    path = f"result/{_now}/sannysoft{_suffix}.png"
    page.screenshot(path=path, full_page=True)

    webbrowser.open(f"file://{Path(path).resolve()}")

df=pd.read_excel('Report complete MFA 6.3.24 ALM UPC w attributes ES Non-Numeric PC ONLY.xlsx',sheet_name='Sales by UPC')
all_prods=list(df['Product'].unique())
all_links=[f"https://www.walmart.com/search?q={i.split(' - ')[0].replace(' ','+')}" for i in all_prods]
# print(all_links)
url=all_links[0]
args = ["--headless=new", "--dump-dom"]
with sync_playwright() as p:
    # browser=p.chromium.launch(headless=False,slow_mo=50)

    browser = p.chromium.launch(args=args)
    context = browser.new_context(locale="en-US")
    Tarnished.apply_stealth(context)

    page = context.new_page()
    # page=browser.new_page()
    page.goto(url)
    element = page.locator("css=div[data-testid='item-stack']")
    first_child = element.locator(">:nth-child(1)")
    first_child.click()
    # children = element.query_selector_all('xpath=child::*')
    # html=page.inner_html('section')
    # soup=BeautifulSoup(html,'html.parser')
    # print(element.inner_html())
    cache_screenshot(page)
    # time.sleep(10000)
