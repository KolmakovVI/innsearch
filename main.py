import os

import undetected_chromedriver as uc

import time


def inn_from_excel():
    inn = "507703578056"
    return inn


def search(inn):
    # driver = uc.Chrome()
    # driver.get("https://www.rusprofile.ru/?1")
    # # os.system('pause') # for CAPCHA
    # search_field = driver.find_element_by_name("query") #work
    # #search_field = driver.find_element(by=By.NAME, value="query") # try to exiqute
    # search_field.send_keys(inn)
    # # how to push the button ????
    # # how to find the button  ????
    # button_field = driver.find_element_by_link_text('Найти')
    # button_field.click()

    #--------------------- second metod: insert INN to url-----------------------------
    url_1 = "https://www.rusprofile.ru/search?query="
    url_2 = "&type=ul"
    full_url = url_1 + inn + url_2
    driver = uc.Chrome()
    driver.get(full_url)


if __name__ == '__main__':
    curr_inn = inn_from_excel()
    search(curr_inn)
    os.system('pause')
