from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, *args):
        by_name, by_val = args[0]
        return self.driver.find_element(by_name, by_val)

    def move_to_element(self):
        return ActionChains(self.driver)
