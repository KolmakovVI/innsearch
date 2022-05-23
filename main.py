import os

import undetected_chromedriver as uc


def search():
    driver = uc.Chrome()
    driver.get("https://www.rusprofile.ru/?1")



if __name__ == '__main__':
    search()
    os.system('pause')
