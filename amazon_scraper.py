from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import undetected_chromedriver as uc
import re
from bs4 import BeautifulSoup

options = uc.ChromeOptions()
options.add_argument("--start-maximized")
options.binary_location = r'C:\Program Files\Google\Chrome Beta\Application\chrome.exe'

browser = uc.Chrome(options = options, service = Service("chromedriver.exe"))

browser.get("https://www.amazon.in/Mode-Red-Tape-Regular-MAT0659_Bright/dp/B09SG419B2/ref=sr_1_95979?qid=1672234965&s=apparel&sr=1-95979&th=1&psc=1")
time.sleep(5)
try:
    element__=browser.find_element('id','inline-twister-expander-header-size_name')
    browser.execute_script("arguments[0].scrollIntoView();", element__)
    button = browser.find_element('id','dimension-expander-icon-size_name')
    class_name=button.get_attribute("class")
    #print(class_name)
    if not "rotate" in class_name:
        button.click()
        print("kano")
except:
    print("button not found")
    time.sleep(500)

all_size=browser.find_element('id','tp-inline-twister-dim-values-container')
# sizes=all_size.find_elements(By.XPAT,"//li[matches(@data-asin,'.*')]")
sizes=all_size.find_elements(By.TAG_NAME,"li")

sizes=list(filter(lambda x :True if x.get_attribute("data-asin") else False  ,sizes))
print(len(sizes))
main_data=[]


for particular_size in sizes:
    kano=particular_size.click()

    time.sleep(2)
    dic={}

    try:

        page_sorce = BeautifulSoup(browser.page_source,"html.parser")
        size_=page_sorce.find('span',id="inline-twister-expanded-dimension-text-size_name").text
        prize=page_sorce.find('span',class_='a-price-whole').text
        discount=page_sorce.find('span',class_='a-size-large a-color-price savingPriceOverride aok-align-center reinventPriceSavingsPercentageMargin savingsPercentage').text
        dic["Size"]=size_
        dic["Prize"]=prize
        dic["Discount"]=discount
        main_data.append(dic)
        # mrp = browser.find_element(By.CLASS_NAME,"a-price a-text-price")
    except:
        print("not found")
        time.sleep(5000)


    # browser.execute_script("arguments[0].scrollIntoView();",mrp)

    time.sleep(10)

print("Loop Is Completed")

print(main_data)
    
time.sleep(5000)




