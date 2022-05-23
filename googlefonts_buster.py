from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from sys import argv

import threading

def googlebuster(e,url):
    driver=webdriver.Firefox()
    driver.get(url)

    driver.implicitly_wait(4)
    print("Site: " + driver.current_url)
    if get_googleapi(driver) == True:
        print("Googleapis found")
    if get_googletag(driver) == True:
        print("Google Tag Manager found")
    if get_googleanalytics(driver) == True:
        print("Google Analytics found")

    driver.close()
    driver.quit()

def get_googleanalytics(driver):
# This is like the third time i did the same thing and it's very ugly, i need to refactor this code
# I'd like a way to dynamically add 
    try:
        elem = driver.find_element(By.XPATH, '//script[contains(@src, "https://www.google-analytics.com")]')
        return True
    except NoSuchElementException:
        return False

def get_googletag(driver):
    try:
        elem = driver.find_element(By.XPATH, '//script[contains(@src, "https://www.googletagmanager.com")]')
        return True
    except NoSuchElementException:
        print("Non trovato!!")
        return False

def get_googleapi(driver):
    try:
        elem = driver.find_element(By.XPATH, '//link[contains(@href, "https://fonts.googleapis.com")]')
        return True
    except NoSuchElementException:
        return False

def main():
    urls=[]

    if (len(argv)>1):
        urls.append(str(argv[1]))

    for url in urls:
        e = threading.Event()
        t = threading.Thread(target=googlebuster, args=(e,url))
        t.start()

    t.join(5)
    exit(0)

if __name__=="__main__":
    main()
