from behave import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.acceptance.locators.blog_page import BlogPageLocators

use_step_matcher('re')


@step('wait for the posts to load')
def step_impl(context):
    try:
        WebDriverWait(context.driver, 10).until(
            expected_conditions.visibility_of_element_located(BlogPageLocators.POSTS_SECTION)
        )
    except:
        print("timed out******")
        raise
