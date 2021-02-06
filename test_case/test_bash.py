from page.app import App


class TestBase():

    def setup(self):
        self.app = App()

    def teardown(self):
        self.app.quit()