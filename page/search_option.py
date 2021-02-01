from page.base_page import BasePage
from page.search_result import SearchResult


class SearchOption(BasePage):
    def goto_search_result(self):
        self.steps("../page/search_option.yml")
        return SearchResult(self._driver)