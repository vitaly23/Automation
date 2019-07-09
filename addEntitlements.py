from Locators import Locator
from selenium.webdriver.support.ui import WebDriverWait


class AddEntitlements:

    def __init__(self, driver, double, char):
        self.driver = driver
        self.char = char
        self.double = float(double)

    def get_page(self):
        self.driver.find_element_by_xpath(Locator.leave_menu_xpath).click()
        self.driver.find_element_by_id(Locator.entitlements_menu_id).click()
        self.driver.find_element_by_id(Locator.leave_addLeaveEntitlement_id).click()

    def find_employee(self):
        WebDriverWait(self.driver, 2)
        elem = self.driver.find_element_by_class_name(Locator.text_field_class_name)
        elem.click()
        elem.clear()
        WebDriverWait(self.driver, 1)
        elem.send_keys('a')
        WebDriverWait(self.driver, 2)
        self.driver.find_element_by_id(Locator.content)
        self.driver.find_element_by_class_name(Locator.ac_even_class_name).click()

    def add_entitlements(self):
        self.driver.find_element_by_id(Locator.text_field_entitlements_id).send_keys("2")
        WebDriverWait(self.driver, 1)
        self.driver.find_element_by_id(Locator.save_button_id).click()

