from selenium.webdriver import Chrome, Firefox
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import getpass
import os

chrome_path = "C:/Users/avsar/OneDrive/Masaüstü/Chrome-Driver/chromedriver"

def headles_for_linux():
    pass

def headless_for_windows():
    chrome_opt = Options()
    chrome_opt.headless = True
    ask_for_consumer = input("Open headless ? [y/n] : ")
    if (ask_for_consumer.lower()) == "y":
        return chrome_opt
    elif (ask_for_consumer.lower()) == "n":
        chrome_opt.headless = False
        return chrome_opt
    else:
        return chrome_opt


class Insta_automate:
    def __init__(self, username, passwd):
        self.username, self.passwd = username, passwd

        self.follow_count = 10

        self.open_instagram()
        self.login()

    def open_instagram(self):
        self.brows = Chrome(executable_path=chrome_path, chrome_options=headless_for_windows()) if os.name == "nt" else Firefox()
        self.brows.get("https://www.instagram.com/")
        self.brows.implicitly_wait(20)
        self.find_username =  self.brows.find_element_by_name("username").send_keys(self.username)
        self.find_passwd = self.brows.find_element_by_name("password").send_keys(self.passwd)

    
    def login(self):
        self.login_but = self.brows.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div").click()
        self.brows.implicitly_wait(20)
        self.dont_save_but = self.brows.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()
        self.brows.implicitly_wait(20)

        try:#if unusing headless this code block will work and close the notification
            self.notification_disable = self.brows.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
            self.brows.implicitly_wait(20)
        except:
            pass

    def hack_with_foll_unfoll(self, seek_name):
        self.brows.get("https://www.instagram.com/{}/".format(seek_name))
        self.brows.implicitly_wait(20)

        def follow():
            self.click_follow = self.brows.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[2]/div/span/span[1]/button").click()
            print("[+] Folloved    > {}".format(seek_name))
            self.delay(7)

        def unfollow():
            self.click_unfollow = self.brows.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[3]/div/span/span[1]/button/div/span").click()
            self.send_enter_to_notfy = self.brows.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[1]")
            self.send_enter_to_notfy.send_keys(Keys.ENTER)
            print("[+] Unfolloved  > {}".format(seek_name))
            self.delay(3)

        try:
            follow()
        except:
            pass
        

        for i in range(self.follow_count):
            print("trying   [ {}/{} ]     ".format(self.follow_count, i))

            unfollow()
            follow()
            


    @staticmethod
    def delay(delay:int):
        for i in range(delay, 0, -1):
            time.sleep(1)
            print("waiting for [{}]  ".format(str(i)), end="\r")


    
if __name__ == "__main__":
    person = Insta_automate(input("Username : "), getpass.getpass())
    for j in range(10):
        person.hack_with_foll_unfoll("cristiano")
        person.hack_with_foll_unfoll("kyliejenner")
        print("THE MAIN LOOP COUNT  >  ", j)
        person.delay(500)

