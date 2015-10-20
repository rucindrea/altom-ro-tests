from base_test import AltomTest


class SmokeTest(AltomTest):

    def setUp(self):
        AltomTest.setUp(self, "firefox")
        self.driver.get("http://altom.ro")
        self.driver.maximize_window()

    def tearDown(self):
        AltomTest.tearDown(self)

    def test_main_test(self):
        assert self.home_page.is_displayed()
        self.screenshot()
