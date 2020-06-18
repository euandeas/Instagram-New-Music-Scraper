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
        time.sleep(4)
        for x in range(2):
            try:
                driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
                time.sleep(4)
            except:
                pass

    def scrapedataslow(self, postsNumber):
        """
        This function handles the scraping of the data from the instagram site and then returns that data as a 2D list, this is alot more accurate, use this at all costs unless not possible.
        """
        scrapeddata = []
        finaldata = []
        driver = self.driver

        #This makes sure all the latest data is loaded from instagram, due to its non chronological nature.
        #for refreshcount in range(10):
            #driver.refresh()
            #time.sleep(2)

        #Loads in extra posts so that the loop can start without throwing any errors due to missing data.
        wholeposts = driver.find_elements_by_xpath("//article[@class='_8Rm4L M9sTE  L_LMM SgTZ1   ePUX4' or @class='_8Rm4L M9sTE  L_LMM SgTZ1  Tgarh ePUX4']")
        webdriver.ActionChains(driver).move_to_element(wholeposts[2]).perform()

        #This increments its way through the posts one by one and scrapes the needed data from each post.
        #This data is then added to a list to be stored.
        for x in range(0, postsNumber):
            print(x)
            #Gathers all currently loaded posts.
            wholeposts = driver.find_elements_by_xpath("//article[@class='_8Rm4L M9sTE  L_LMM SgTZ1   ePUX4' or @class='_8Rm4L M9sTE  L_LMM SgTZ1  Tgarh ePUX4']")
            
            moreButtonsLeft = True
            while moreButtonsLeft == True:
                try:
                    morebutton = driver.find_element_by_xpath("//span[@class='_8Pl3R']").find_element_by_xpath("//button[@class='sXUSN']")
                    driver.execute_script("arguments[0].click();", morebutton)
                except:
                    moreButtonsLeft = False
            
            for post in wholeposts:
                username = ""
                date = ""
                desc = ""

                try:
                    username = post.find_element_by_xpath("//a[@class='sqdOP yWX7d     _8A5w5   ZIAjV ']").text
                except:
                    pass
                try:
                     date = post.find_element_by_xpath("//time[@class='_1o9PC Nzb55']").text
                except:
                    pass
                try:
                    desc = post.find_element_by_xpath("//span[@class='_8Pl3R']").text
                except:
                    pass

                scrapeddata.append([username, desc, date])
                time.sleep(0.5)
            
            time.sleep(1)
            #This is the part which moves the posts along.
            try:
                webdriver.ActionChains(driver).move_to_element(wholeposts[6]).perform()  
            except:
                try:
                    webdriver.ActionChains(driver).move_to_element(wholeposts[5]).perform()
                except:
                    webdriver.ActionChains(driver).move_to_element(wholeposts[4]).perform()
            time.sleep(2)

        for x in scrapeddata:
            if x not in finaldata:
                if x != ["","",""]:
                    finaldata.append(x)

        return finaldata

    def __init__(self):
        self.driver = self.__BootDriver()
        self.__Login(self.driver)
   
