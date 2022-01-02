from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"

USERNAME = "..."
PASSWORD = "..."
SIMILAR_ACCOUNT = "the IG account you want to follow their followers"

INSTAGRAM = "https://www.instagram.com/accounts/login/"
TARGET_PROFILE = f"https://www.instagram.com/{SIMILAR_ACCOUNT}/"

class InstaFollower:
    def __init__(self, driver_path):
        self.serv = Service(driver_path)
        self.driver = webdriver.Chrome(service=self.serv)

    def login(self, url):
        self.driver.get(url)

        cookies = self.driver.find_element(By.CLASS_NAME, "aOOlW.bIiDR")
        cookies.click()

        username = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        username.send_keys(USERNAME)

        password = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)
        sleep(2)

        notification = self.driver.find_element(By.CLASS_NAME, 'aOOlW.HoLwm')
        notification.click()
        sleep(1)
        # cookies = self.driver.find_element(By.CLASS_NAME, 'aOOlW.bIiDR')
        # cookies.click()

    def find_followers(self, url):
        sleep(2)
        self.driver.get(url)
        sleep(2)
        followers = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        sleep(1)

        modal = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div[2]')

        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(2)

    def follow(self):
        follow_buttons = self.driver.find_elements(By.CLASS_NAME, 'sqdOP.L3NKy.y3zKF')

        for button in follow_buttons:
            try:
                sleep(1)
                button.click()
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div[3]/button[2]')
                cancel_button.click()



bot = InstaFollower(CHROME_DRIVER_PATH)

bot.login(INSTAGRAM)
bot.find_followers(TARGET_PROFILE)
bot.follow()