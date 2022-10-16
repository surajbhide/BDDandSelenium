from selenium.webdriver.common.by import By

from tests.acceptance.locators.base_page import BasePageLocator


class BlogPageLocators(BasePageLocator):
    ADD_POST_LINK = By.ID, "add-post-link"
    POSTS_SECTION = By.ID, "posts"
    POST = By.CLASS_NAME, "post-link"
