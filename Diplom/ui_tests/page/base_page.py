from time import sleep

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config.config import Config

config = Config.load_from_json()


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, config.explicit_wait)

    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click_element(self, locator):
        element = self.find_element(locator)
        element.click()

    def get_text_element(self, locator):
        element = self.find_element(locator)
        return element.text

    def send_keys_to_element(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def assert_field_value(self, locator, expected_value):
        element = self.find_element(locator)
        assert element.get_attribute(
            'value') == expected_value, f"Expected value: {expected_value}, but got: {element.get_attribute('value')}"

    def assert_element_contains_text(self, locator, expected_text):
        element = self.find_element(locator)
        actual_text = element.text
        assert expected_text in actual_text, f"Expected text '{expected_text}' not found in element text '{actual_text}'"

    def scroll_down(self):
        """A method for scrolling the page down using ActionChains."""
        actions = ActionChains(self.driver)
        actions.scroll_by_amount(0, 400).perform()
        sleep(1)  # Wait to ensure the scroll action is completed

    def scroll_up(self):
        """A method for scrolling the page up."""
        self.driver.execute_script("window.scrollTo(0, 0);")
        sleep(1)  # Wait to ensure the scroll is completed

    def assert_url(self, expected_url):
        actual_url = self.driver.current_url
        assert expected_url in actual_url, f"Expected text '{expected_url}' not found in current URL '{actual_url}'"

    def wait_element_is_displayed(self, locator):
        self.find_element(locator)
