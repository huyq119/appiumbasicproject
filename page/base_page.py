import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page.handle_black import handle_black


class BasePage():
    _driver: WebDriver = None

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    @handle_black
    def find(self, locator, value):
        element = self._driver.find_element(locator, value)
        locator1 = (locator, value)
        WebDriverWait(self._driver, 2).until(expected_conditions.element_to_be_clickable(locator1))
        return element

    def steps(self, path):
        with open(path) as f:
            _steps = yaml.safe_load(f)
        for _step in _steps:
            if "by" in _step.keys():
                _element = self.find(_step["by"], _step["locator"])
            if "action" in _step.keys():
                _action = _step["action"]
                if _action == "click":
                    _element.click()
                if _action == "send_keys":
                    _element.send_keys(_step["value"])

        return self
