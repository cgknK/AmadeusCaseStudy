import time, os, random

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait

def return_cities_list():
    # Bakılacak yerin önce temizlenmesi gerekebilir
    from_side_btn = driver.find_element(By.ID, "headlessui-combobox-button-:R1a9lla:")
    from_side_btn.click()
    from_side_btn_values = driver.find_element(By.ID, "headlessui-combobox-options-:R1q9lla:")
    cities = from_side_btn_values.text.split("\n")
    new_cities = []
    for i, j in enumerate(cities):
        if i % 2 == 0:
            new_cities.append(j)
    return new_cities

def write_from_side(string, element_id="headlessui-combobox-input-:Rq9lla:"):
    from_side = driver.find_element(By.ID, element_id)
    from_side.send_keys(string)
    from_side.send_keys(Keys.ENTER)

def write_to_side(string, element_id="headlessui-combobox-input-:Rqhlla:"):
    to_side = driver.find_element(By.ID, element_id)
    to_side.send_keys(string[:3])
    to_side.send_keys(Keys.ENTER)

def read_from_side(element_id="headlessui-combobox-input-:Rq9lla:"):
    from_side = driver.find_element(By.ID, element_id)
    return from_side.get_attribute("value")

def read_to_side(element_id="headlessui-combobox-input-:Rqhlla:"):
    to_side=driver.find_element(By.ID, element_id)
    return to_side.get_attribute("value")

def count_by_text(css_selector="p.mb-10"):
    write_from_side("ist")
    write_to_side("los")
    found_x_items = driver.find_element(By.CSS_SELECTOR, css_selector)
    found_x_items = found_x_items.text.split(" ")
    number = ""
    for i in found_x_items:
        # Regex kullanmak daha mantıklı
        try:
            if type(int(i)) == int:
                number += i
        except:
            pass
        else:
            number = int(number)
    return number

def count_tables(copy_selector=
     r"body > main > div.mt-24.max-w-5xl.w-full.justify-center.items-center.text-sm.lg\:flex > div > ul"):
    write_from_side("ist")
    write_to_side("los")
    table_items_ul = driver.find_element(By.CSS_SELECTOR, copy_selector)
    table_items_inner_ul = table_items_ul.find_elements(By.TAG_NAME, "li")
    return len(table_items_inner_ul)


if __name__ == "__main__":
    service = Service('./chromedriver-win64/chromedriver.exe')
    driver = webdriver.Chrome(service=service)

    driver.maximize_window()

    test_link = 'https://flights-app.pages.dev/'

    driver.get(test_link)
    page_link = driver.current_url
    page_title = driver.title
    print(page_title, page_link)

    time.sleep(1)
