from selenium import webdriver
import os
import time

def BootDriver():
    currentPath = (os.path.abspath(os.getcwd()))
    try:
        driver = webdriver.Chrome(currentPath + "\\Drivers\\chromedriver.exe")
    except:
        driver = webdriver.Chrome(currentPath + "\\Drivers\\operadriver.exe")
    
    driver.get("https://www.instagram.com")
    time.sleep(2)
    return driver

def Login(driver):
    driver.find_element_by_name("username").send_keys("")
    driver.find_element_by_name("password").send_keys("")
    driver.find_element_by_xpath("//button[@type='submit']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
    time.sleep(5)

driver = BootDriver()
Login(driver)


