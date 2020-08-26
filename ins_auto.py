from selenium.webdriver import Chrome
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

import time
import getpass

chrome_path = "C:/Users/avsar/OneDrive/Masaüstü/Chrome-Driver/chromedriver"

class Insta_automate:
    def __init__(self, username, passwd):
        self.username, self.passwd = username, passwd
        self.open_instagram()
        self.login()

    def open_instagram(self):
        self.brows = Chrome(executable_path=chrome_path)
        self.brows.get("https://www.instagram.com/")
        self.brows.implicitly_wait(20)
        self.find_username =  self.brows.find_element_by_name("username")
        self.find_passwd = self.brows.find_element_by_name("password")
        self.find_username.send_keys(self.username)
        self.find_passwd.send_keys(self.passwd)
    
    def login(self)
        self.login_but = self.brows.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div").click()
        self.brows.implicitly_wait(20)
        self.dont_save_but = self.brows.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()
        self.brows.implicitly_wait(20)
        self.notification_disable = self.brows.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
        self.brows.implicitly_wait(20)    

    def hack_with_foll_unfoll(self, seek_name):
        self.search_bar = self.brows.find_element_by_xpath("")


    

    

    
if __name__ == "__main__":
    person = Insta_automate("avsarhalilibrahim", getpass.getpass())
    time.sleep(50)
