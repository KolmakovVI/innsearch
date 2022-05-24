import os

import undetected_chromedriver as uc


def inn_from_excel():
    inn = "507703578056"
    return inn


def search(inn):
    driver = uc.Chrome()
    driver.get("https://www.rusprofile.ru/?1")
    os.system('pause') # for CAPCHA
    search_field = driver.find_element_by_name("query") #work
    #search_field = driver.find_element(by=By.NAME, value="query") # try to exiqute
    search_field.send_keys(inn)
    # how to push the button ????
    # how to find the button  ????
    #button_field = driver.find_element_by_class_name('search-btn waves-effect waves-light')


if __name__ == '__main__':
    curr_inn = inn_from_excel()
    search(curr_inn)
    os.system('pause')
