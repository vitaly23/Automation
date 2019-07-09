from Locators import Locator
from selenium.webdriver.support.ui import WebDriverWait


class TableElements:

    def __init__(self, driver):
        self.driver = driver
        self.col_0 = []
        self.driver.find_element_by_id(Locator.menu_admin_id).click()
        self.driver.find_element_by_id(Locator.menu_UserManagement_id).click()
        self.driver.find_element_by_id(Locator.menu_viewSystemUsers_id).click()
        WebDriverWait(driver, 2)

    def add_col_0(self):
        for i in range(1,20):
            element = self.driver.find_elements_by_xpath("//a[contains(@href,'saveSystemUser?userId=')]")
            for elem in element:
                self.col_0.append(elem.get_attribute('text'))

    def return_list_of_names(self):
        return self.col_0


