from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from InstaCred import usname
from InstaCred import pswd

class Insta:
    def __init__(self,usname,pswd):
        self.driver= webdriver.Chrome()
       # self.driver.get("https://www.instagram.com/accounts/emailsignup/?hl=en")
        self.driver.get("https://instagram.com")
        sleep(10)
       
        self.driver.find_element("xpath","//input[@name=\"username\"]")\
            .send_keys(usname)
        self.driver.find_element("xpath","//input[@name=\"password\"]")\
            .send_keys(pswd)
        self.driver.find_element("xpath",'//button[@type="submit"]')\
            .click()
        print("I'm In")
        sleep(5)
        self.driver.find_element("xpath","//button[contains(text(), 'Not now')]")\
            .click()
        sleep(5)
        self.driver.find_element("xpath","//button[contains(text(), 'Not Now')]")\
            .click()
        sleep(10)
    
    def find_unfollowers(self):
        i,j=0,1
        self.driver.find_element("xpath","//a[contains(@href,'/{}')]".format(self.usname))\
            .click()
        self.driver.find_element("xpath","//a[contains(@href,'/following')]")\
            .click()
        sugg=self.driver.find_element("xpath",'//h4[contains,text(),Suggestions)]')
        self.driver.execute_script('arguements[0].scrollIntoView()',sugg)
        sleep(2)
        
        while(i!=j):
            i=j
            sleep(1)
            i=self.driver.execute_script(



bot=Insta(usname,pswd)