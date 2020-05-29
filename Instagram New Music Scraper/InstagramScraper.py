from selenium import webdriver
import os
import time
import getpass


class InstagramScraper():

    def __BootDriver(self):
        """
        This fucntion loads the selenium webdriver and then loads up instagram and returns the driver to be used in other functions. 
        It defaults to using the chrome driver if it is present and if not i have set it to use opera driver as this is my browser of choice.
        """
        currentPath = (os.path.abspath(os.getcwd()))
        try:
            driver = webdriver.Chrome(currentPath + "\\Drivers\\chromedriver.exe")
        except:
            driver = webdriver.Chrome(currentPath + "\\Drivers\\operadriver.exe")
    
        driver.get("https://www.instagram.com")
        time.sleep(2)
        return driver

    def __Login(self, driver):
        """
        This procedure setups the instagram page by handling login and any popups that may occur after login.
        """
        driver.find_element_by_name("username").send_keys(input("Enter Username: "))
        driver.find_element_by_name("password").send_keys(getpass.getpass("Enter Password: "))
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        time.sleep(5)

    def scrapedata(self, postsNumber):
        """
        This function handles the scraping of the data from the instagram site and then returns that data as a 2D list.
        """
        scrapeddata = []
        finaldata = []
        driver = self.driver

        #Loads in extra posts so that the loop can start without throwing any errors due to missing data.
        wholeposts = driver.find_elements_by_xpath("//article[@class='_8Rm4L M9sTE  L_LMM SgTZ1   ePUX4' or @class='_8Rm4L M9sTE  L_LMM SgTZ1  Tgarh ePUX4']")
        webdriver.ActionChains(driver).move_to_element(wholeposts[2]).perform()

        #This increments its way through the posts one by one and scrapes the needed data from each post.
        #This data is then added to a list to be stored.
        for x in range(0, postsNumber):
            #Gathers all currently loaded posts.
            wholeposts = driver.find_elements_by_xpath("//article[@class='_8Rm4L M9sTE  L_LMM SgTZ1   ePUX4' or @class='_8Rm4L M9sTE  L_LMM SgTZ1  Tgarh ePUX4']")
        
            #Scrapes data from top loaded post
            username = driver.find_element_by_xpath("//a[@class='FPmhX notranslate MBL3Z']").text
            try:
                driver.execute_script("arguments[0].click();", driver.find_element_by_xpath("//span[@class='_8Pl3R']").find_element_by_xpath("//button[@class='sXUSN']"))
            except:
                pass
            desc = driver.find_element_by_xpath("//span[@class='_8Pl3R']").text

            date = driver.find_element_by_xpath("//time[@class='_1o9PC Nzb55']").text

            scrapeddata.append([username, desc, date])

            #This is the part which moves the posts along.
            try:
                webdriver.ActionChains(driver).move_to_element(wholeposts[5]).perform()
            except:
                webdriver.ActionChains(driver).move_to_element(wholeposts[4]).perform()
            time.sleep(2)

        for x in scrapeddata:
            if x not in finaldata:
                finaldata.append(x)

        return finaldata

    def __init__(self):
        self.driver = self.__BootDriver()
        self.__Login(self.driver)
   
