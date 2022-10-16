from tests.acceptance.locators.base_page import BasePageLocator


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return 'http://127.0.0.1:5000'

    @property
    def title(self):
        return self.driver.find_element(*BasePageLocator.TITLE)

    @property
    def navigation(self):
        return self.driver.find_elements(*BasePageLocator.NAV_LINKS)
