from Locators import Locator
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username = "Admin"
        self.password = "admin123"

    def enter_username(self):
        self.driver.find_element_by_id(Locator.username_textbox_id).clear()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, Locator.username_textbox_id )))
        self.driver.find_element_by_id(Locator.username_textbox_id).send_keys(self.username)
        WebDriverWait(self.driver, 5)

    def enter_password(self):
        self.driver.find_element_by_id(Locator.password_textbox_id).clear()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID,Locator.password_textbox_id )))
        self.driver.find_element_by_id(Locator.password_textbox_id).send_keys(self.password)
        WebDriverWait(self.driver, 5)

    def click_login(self):
        self.driver.find_element_by_id(Locator.login_button_id).click()
        time.sleep(3)

    def click_logout(self):
        self.driver.find_element_by_link_text(Locator.welcome_link_name).click()
        WebDriverWait(self.driver, 1.5)
        self.driver.find_element_by_link_text(Locator.logout_link_text).click()
        WebDriverWait(self.driver, 5)

