from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from datetime import datetime
from selenium.webdriver.common.keys import Keys
import time


class TikTok:

    def __init__(self, username):
        self.username = username

    def get_er_reach(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome_options)
        er_dict = {}
        reach_dict = {}
        for uname in self.username:
            driver.get(f"https://hypeauditor.com/tiktok/{uname}/")
            soup = BeautifulSoup(driver.page_source, "html.parser")
            try:
                er_tag = soup.find_all(class_="metric metric")[2].getText()
                reach_tag = soup.find_all(class_="metric metric")[1].getText()
            except IndexError:
                er_dict[uname] = "Profile doesn't exist"
                reach_dict[uname] = "Profile doesn't exist"
            else:
                er = er_tag.replace("ER\xa0\uf059", "").strip("%")
                reach = reach_tag.replace("Avg. Views per post\xa0\uf059", "")
                er_dict[uname] = float(er)
                reach_dict[uname] = reach

        driver.close()
        return er_dict, reach_dict
