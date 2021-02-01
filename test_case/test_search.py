from page.app import App


class TestSearch():

    def setup(self):
        self.app = App()

    def test_search(self):
        self.app.start().main().goto_search().goto_search_option().goto_search_result()

    def teardown(self):
        self.app.quit()