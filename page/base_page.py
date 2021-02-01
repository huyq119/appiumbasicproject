import yaml
from appium.webdriver.webdriver import WebDriver


class BasePage():
    _driver: WebDriver = None

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, locator, value):
        return self._driver.find_element(locator, value)

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

