import pandas as pd
import undetected_chromedriver as uc
import time
from selenium.webdriver.common.by import By
# driver = uc.Chrome(headless=False,use_subprocess=False)

dt=1


if __name__=='__main__':
    df=pd.read_excel('Report complete MFA 6.3.24 ALM UPC w attributes ES Non-Numeric PC ONLY.xlsx',sheet_name='Sales by UPC')
    all_prods=list(df['Product'].unique())
    all_links=[f"https://www.walmart.com/search?q={i.split(' - ')[0].replace(' ','+')}" for i in all_prods]
    connections={}
    # # print(all_links)
    # url=all_links[0]
    # url='https://www.walmart.com/search?q=LAYS+POTATO+CHIP+CLASSIC+BAG+8+OZ'
    # print(url)
    options = uc.ChromeOptions()  
    options.add_argument(r"--user-data-dir=C:\Users\TheQwertyPhoenix\AppData\Local\Google\Chrome\User Data")
    options.add_argument('--profile-directory=Profile 1') #e.g. Profile 3
    driver=uc.Chrome(options=options)
    # time.sleep(10000)
    print(len(all_links))
    for url in all_links:
        print(url)
        driver.get(url)
        element = driver.find_element(By.CSS_SELECTOR, "div[data-testid='item-stack']")
        # element.find_element(By.CSS_SELECTOR, ">:nth-child(1)").click()
        allprods=element.find_elements(By.XPATH, "./*")
        allprods[0].click()
        time.sleep(5)
        
        images = driver.find_elements(By.CSS_SELECTOR, "img")
        time.sleep(5)
        print('------------------------------------------------------------')
        print(images)
        time.sleep(dt)
        # print([i.get_attribute('outerHTML') for i in images])
        # print(element.get_attribute('innerHTML'))
        try:
            connections[url]=[i.get_attribute('outerHTML') for i in images]
        except:
            print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
            connections[url]=[]

        pd.DataFrame(connections).to_csv('scraped.csv')
        # time.sleep(10000)
    # print(connections)
