import time, os, random

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait

service = Service('./chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=service)

# flights
print("flights")
driver.get('https://flights-app.pages.dev/')
page_link = driver.current_url
print("page_url: ", page_link)
page_title = driver.title
print("page_title: ", page_title)
state_window = driver.maximize_window()
print(state_window, "state_window")

#google
print("google")
driver.get('https://www.google.com/')
page_link = driver.current_url
print("page_url: ", page_link)
page_title = driver.title
print("page_title: ", page_title)

print("\n")
#time.sleep(0.5)
driver.back()
page_title = driver.title
print("BACKpage_title: ", page_title)
#time.sleep(0.5)
driver.forward()
page_title = driver.title
print("page_title: ", page_title)
#time.sleep(0.3)
driver.refresh()
page_title = driver.title
print("page_title: ", page_title)
#time.sleep(0.3)
driver.refresh()
page_title = driver.title
print("page_title: ", page_title)
#time.sleep(1)
if "flights-app.pages" in page_link:
    print("Wrong page")
else:
    if not os.path.exists("./res"):
        os.mkdir("./res")
    else:
        for file in os.listdir("./res"):
            file_path = os.path.join("./res", file)
            os.remove(file_path)
    #driver.save_screenshot("./else_deneme.jpg")
    driver.save_screenshot("./res/else_deneme_line45.png")

"""
driver.close()
driver.quit()
"""


#from_side_icin = driver.find_element(By.ID, "headlessui-combobox-button-:R1a9lla:")
#from_side_icin.click()
#driver.find_element(By.ID, "headlessui-combobox-button-:R1a9lla:").click()
time.sleep(2)
from_side_list = driver.find_elements(By.ID, "headlessui-combobox-options-:R1q9lla:")
#wait = WebDriverWait(driver, 1)
city = "istanbul"
citys = "headlessui-combobox-options-:R1q9lla:"
citys = driver.find_elements(By.ID, "headlessui-combobox-options-:R1q9lla:")
print("citys")
print(citys)
print("for")
for i in citys:
    print(i.text)
    print(i.get_attribute("value"))
    print(i.get_attribute("innerText"))

hata1a = 0
hata1b = 0

print("\nfocus\n")
driver.back()
from_side = driver.find_element(By.ID, "headlessui-combobox-input-:Rq9lla:")
print("from_side:", from_side)
from_side.send_keys(city)
from_side.send_keys(Keys.ENTER)

to_side = driver.find_element(By.ID, "headlessui-combobox-input-:Rqhlla:")
to_side.send_keys(city[:3])

#wait = WebDriverWait(driver, 1.5)
li_element = driver.find_elements(By.ID, "headlessui-combobox-option-:r7:")
print("\nprintlielement", li_element, li_element[0])
for i in li_element:
    word = i.text[:].lower()
    word2 = i.get_attribute("value").lower()
    print("word: ", word)
    print("word2: ", word2)
    if city in word or city in word2:
        hata1a = 1
        print("hata1a")
    else:
        print(i.text.lower())

durum_to_side = to_side.send_keys(Keys.ENTER)
if to_side.get_attribute("value").lower() == city.lower():
    hata1b = 1
    print("hata1b")
else:
    print(city.lower(), "to_side.text0")
    print(to_side.text.lower(), "to_side.text1")
print("durum_to_side", durum_to_side)

if hata1a and hata1b:
    print("1. test hatası ss falan")
elif hata1a or hata1b:
    print("1 hatada sorun var")
else:
    print("hatayi bulmadi")

print(hata1a, hata1b)


print("\nfocus2\n")
driver.refresh()
#from_list_button = driver.find_elements(By.ID, "headlessui-combobox-button-:R1a9lla:")
#from_list_button.click()
#driver.find_elements(By.ID, "headlessui-combobox-button-:R1a9lla:").click()
elements = driver.find_elements(By.ID, "headlessui-combobox-button-:R1a9lla:")
elements[0].click()
#elements[0].click()
#elements[0].send_keys(Keys.ENTER)

ul_element = driver.find_elements(By.ID, "headlessui-combobox-options-:R1q9lla:")
print("\nprintlielement", ul_element, ul_element[0])
for i in ul_element:
    word = i.text[:].lower()
    #word2 = i.get_attribute("value").lower()
    print("word: ", word)
    #print("word2: ", word2)
    if city in word or city in word2:
        hata1a = 1
        print("hata1a")
    else:
        print(i.text.lower())

#random.choice(ul_element).click()
ul_element[0].click()

#find_element X not s X
temp_text = driver.find_element(By.ID, "headlessui-combobox-input-:Rq9lla:")
elements2 = driver.find_elements(By.ID, "headlessui-combobox-button-:R1ahlla:")
elements2[0].click()
ul_element2 = driver.find_elements(By.ID, "headlessui-combobox-options-:R1qhlla:")
for i in ul_element2:
    print("elements[0].text not in i.text[:]", temp_text.get_attribute("innerText"))

    if temp_text.get_attribute("innerText") not in i.text[:] and 0:
        pass
    else:
        #elements2[0].send_keys(f"{elements2[0].text}")
        elements2[0].send_keys("Tokyo")
        elements2[0].send_keys(Keys.ENTER)
        #elements2[0].click()

time.sleep(1.25)

#driver.find_element(By.ID, "headlessui-combobox-option-:r1s:").click()

okunacak_sayi = driver.find_element(By.CSS_SELECTOR, "p.mb-10")
print(okunacak_sayi.get_attribute("innerText"))

time.sleep(1)

#to_list = driver.find_element(By.ID, "headlessui-combobox-option-:r1q:").click()
#print("to list:", to_list)
"""
to_list = driver.find_element_by_xpath("//li[@id='headlessui-combobox-option-:r1r:']")
next_xpath = "//li[@id='headlessui-combobox-option-:r1r:']/following-sibling::span[0]"
next_sibling = driver.find_element_by_xpath(next_xpath)
print(next_sibling)
next_xpath = "//li[@id='headlessui-combobox-option-:r1r:']/following-sibling::span[1]"
next_sibling = driver.find_element_by_xpath(next_xpath)
print(next_sibling)
"""
