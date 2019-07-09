from selenium import webdriver
import unittest
import os
import logging
from Locators import Locator
from Login_Page import LoginPage
from preformance_menu import PerformanceMenu
from threading import Lock
from usersTable import UsersTable
from selenium.webdriver.support.ui import WebDriverWait
from testLink import TestLink
from addEntitlements import AddEntitlements


class ArmisTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # creating a logger
        cls.logger = logging.getLogger('test')
        cls.logger.setLevel(logging.DEBUG)
        cls.logger.c_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # create file handler which logs messages
        fh = logging.FileHandler('result.log')
        cls.logger.addHandler(fh)
        # a simple lock for asyncronic purposes
        cls.lock = Lock()

        # attaching the chromedriver to selenium and initial set up
        cls.dir_path = os.path.dirname(os.path.realpath(__file__))
        cls.chrome_driver = cls.dir_path + '/chromedriver'
        cls.driver = webdriver.Chrome(cls.chrome_driver)
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.login_page = LoginPage(cls.driver)
        cls.link_tester = TestLink(cls.driver)
        cls.add_entitlements = AddEntitlements(cls.driver,int(2.00), 'a')
        cls.driver.get(Locator.website_url)

    def test_00_login(self):
        try:
            self.lock.acquire()
            self.login_page = LoginPage(self.driver)
            self.login_page.enter_username()
            self.login_page.enter_password()
            self.login_page.click_login()
            assert self.driver.current_url == Locator.homepage_url
        except AssertionError:
            self.logger.debug('Login test failed.')
        else:
            self.logger.debug("Login test succeeded.")
        finally:
            self.lock.release()

    def test_01_performance_menu(self):
        try:
            self.lock.acquire()
            self.performance_menu = PerformanceMenu(self.driver)
            self.performance_menu.click_performance_menu()
            self.performance_menu.click_configure()
            self.performance_menu.click_KPI()
            assert self.driver.current_url == Locator.kpi_page_url
        except AssertionError:
            self.logger.debug('Login test failed.')
        else:
            self.logger.debug("Login Test Complete successfully")
        finally:
            self.lock.release()

    def test_02_getTableInfo(self):
        self.lock.acquire()
        try:
            self.users_table = UsersTable(self.driver)
            super(UsersTable,self.users_table).add_col_0()
            self.table = self.users_table.return_list()
            self.logger.debug("List of all elements:\n")
            for item in self.table:
                self.logger.debug(item +"\n")
        finally:
            self.lock.release()

    def test_03_scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        WebDriverWait(self.driver, 1.5)

    def test_04_add_entitlements(self):
        self.lock.acquire()
        try:
            self.add_entitlements.get_page()
            self.add_entitlements.find_employee()
            self.add_entitlements.add_entitlements()
        finally:
            self.lock.release()

    def test_05_get_to_projects_page(self):
        self.lock.acquire()
        try:
            WebDriverWait(self.driver,5)
            self.driver.find_element_by_id(Locator.project_info_id).click()
            self.driver.find_element_by_link_text(Locator.projects_link_text)
        except AssertionError:
            self.logger.debug("Projects page access failed")
        else:
            self.logger.debug("Projects page access failed")
        finally:
            self.lock.release()

    def test_06_get_to_job_vacancies_page(self):
        self.lock.acquire()
        try:
            self.driver.find_element_by_link_text(Locator.recruitment_link_text).click()
            self.driver.find_element_by_link_text(Locator.vacancies_link_text).click()
        except AssertionError:
            self.logger.debug("Vacancies page access failed")
        else:
            self.logger.debug("Vacancies page access failed")
        finally:
            self.lock.release()

    def test_07_logout(self):
        self.lock.acquire()
        try:
            WebDriverWait(self.driver, 5)
            self.logger.debug("logging out")
        except AssertionError:
            self.logger.debug("Logout access failed")
        else:
            self.logger.debug("Logout access failed")
        finally:
            self.login_page.click_logout()
            self.lock.release()
            WebDriverWait(self.driver, 2)


    def test_08_check_original_website_link(self):
        self.lock.acquire()
        try:
            WebDriverWait(self.driver, 5)
            self.link_tester.click_link()
            WebDriverWait(self.driver, 5)
        except AssertionError:
            self.logger.debug("Original page access failed")
        else:
            self.logger.debug("Original page access failed")
        finally:
            self.lock.release()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
