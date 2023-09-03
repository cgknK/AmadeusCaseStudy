import time, os, random

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait

service = Service('./chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.maximize_window()

driver.get('https://flights-app.pages.dev/')
page_link = driver.current_url
page_title = driver.title
print(page_title, page_link)

from_side = driver.find_element(By.ID, "headlessui-combobox-input-:Rq9lla:")
#from_side.click()

from_side_btn = driver.find_element(By.ID, "headlessui-combobox-button-:R1a9lla:")
from_side_btn.click()
from_side_btn_values = driver.find_element(By.ID, "headlessui-combobox-options-:R1q9lla:")
cities = from_side_btn_values.text.split("\n")

to_side = driver.find_element(By.ID, "headlessui-combobox-input-:Rqhlla:")

for city in cities:
    from_side.send_keys(city)
    from_side.send_keys(Keys.ENTER)
    to_side.send_keys(city[:3])
    to_side.send_keys(Keys.ENTER)
    if to_side.get_attribute("value") == city:
        print("hata1")
        break
    #refresh ve tamamını kontrol etmek için düzeltme gerekli(wrap by while)
    # yada tanımlamalar sıfırlanıyor olabilir refresh'den sonra
    driver.refresh()


driver.refresh()

from_side = driver.find_element(By.ID, "headlessui-combobox-input-:Rq9lla:")
from_side.send_keys("ist")
from_side.send_keys(Keys.ENTER)
to_side = driver.find_element(By.ID, "headlessui-combobox-input-:Rqhlla:")
to_side.send_keys("los")
to_side.send_keys(Keys.ENTER)

found_x_items = driver.find_element(By.CSS_SELECTOR, "p.mb-10")
found_x_items = found_x_items.text.split(" ")
number = -1
for i in found_x_items:
    # Regex kullanmak daha mantıklı
    try:
        if type(int(i)) == int:
            number = int(i)
            print(number)
    except:
        pass

table_items_css_class = "grid grid-cols-1 gap-x-6 gap-y-8 lg:grid-cols-3 xl:gap-x-8"
copy_selector = r"body > main > div.mt-24.max-w-5xl.w-full.justify-center.items-center.text-sm.lg\:flex > div > ul"
table_items_ul = driver.find_element(By.CSS_SELECTOR, copy_selector)
table_items_inner_ul = table_items_ul.find_elements(By.TAG_NAME, "li")
print(type(table_items_inner_ul))
print(len(table_items_inner_ul))
if number == len(table_items_inner_ul):
    pass
else:
    print("hata2")
#print(len(table_items))

#/html/body/main/div[2]/div/ul

time.sleep(1)