from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

import threading

def googlebuster(e,url):
    driver=webdriver.Firefox()
    driver.get(url)

    driver.implicitly_wait(2)
    if get_googleapi(driver) == True:
        print("Googleapis found on " + driver.current_url)

    driver.close()
    driver.quit()

def get_googleapi(driver):
    try:
        elem = driver.find_element(By.XPATH, '//link[contains(@href, "https://fonts.googleapis.com")]')
        return True
    except NoSuchElementException:
        return False

def main():
    urls=["http://www.example.com"]

    for url in urls:
        e = threading.Event()
        t = threading.Thread(target=googlebuster, args=(e,url))
        t.start()

    t.join(5)
    exit(0)

if __name__=="__main__":
    main()
