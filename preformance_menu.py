from Locators import Locator
import time


class PerformanceMenu():

    def __init__(self,driver):
        self.driver = driver

    def click_performance_menu(self):
        self.driver.find_element_by_id(Locator.menu_performance_id).click()

    def click_configure(self):
        self.driver.find_element_by_id(Locator.menu_performance_Configure_id).click()

    def click_KPI(self):
        self.driver.find_element_by_id(Locator.menu_performance_searchKpi_id).click()
        time.sleep(2)
        assert(self.driver.current_url == Locator.kpi_page_url)


