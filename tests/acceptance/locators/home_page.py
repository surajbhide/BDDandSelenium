from selenium.webdriver.common.by import By

from tests.acceptance.locators.base_page import BasePageLocator


class HomePageLocators(BasePageLocator):
    NAVIGATION_LINK = By.ID, "blog-link"
