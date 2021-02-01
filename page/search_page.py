from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page.base_page import BasePage
from page.search_option import SearchOption


class SearchPage(BasePage):

    def goto_search_option(self):
        self.steps("../page/search.yml")
        _ele = WebDriverWait(self._driver, 10)
        _locator = (MobileBy.ID, "com.xueqiu.android:id/name")
        _ele.until(expected_conditions.element_to_be_clickable(_locator))
        return SearchOption(self._driver)