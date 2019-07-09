
class TestLink:

    def __init__(self,driver):
        self.driver = driver

    def click_link(self):
        self.driver.find_element_by_tag_name('a').click()
