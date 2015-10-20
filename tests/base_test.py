__author__ = 'rucindrea'

import datetime
from selenium.webdriver import FirefoxProfile, Firefox, ChromeOptions, Chrome
from pages import home
import unittest
import os


class AltomTest(unittest.TestCase):
    driver = None
    home_page = None

    def setUp(self, browser):
        self.browser = browser

        if "firefox" in self.browser:
            profile = FirefoxProfile()
            # profile.set_preference("plugin.state.silverlight", 2)
            # profile.set_preference("browser.download.folderList", 1)
            # profile.set_preference("pdfjs.disabled", False);
            # profile.set_preference("pdfjs.firstRun", True);
            self.driver = Firefox(profile)  # get a new firefox session

        if "chrome" in self.browser:
            chromedriver = "/usr/local/bin/chromedriver"
            options = ChromeOptions()
            options.add_experimental_option('excludeSwitches', ['disable-component-update'])
            options.add_argument("--user-data-dir=./browser_resources/chrome_data_dir/")
            os.environ["webdriver.chrome.driver"] = chromedriver
            self.driver = Chrome(executable_path=chromedriver, chrome_options=options)

        self.home_page = home.Home(self.driver)

    def tearDown(self):
        self.driver.quit()

    def screenshot(self, name='.'):
        if name == '.':
            name = self.browser
        now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        name = '%s-%s.png' % (name, now)
        output_path = "../test_results/screenshots/"
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        retries = 5
        for r in xrange(retries):
            try:
                self.driver.get_screenshot_as_file(output_path + name)
                break
            except Exception as e:
                print "retry to take screenshot: %d out of %d" % (r + 1, retries)
                print e.message
                if r == retries - 1:
                    print "ERROR: failed to take screenshot"
        print "screenshot saved with file name: %s" %name
        return name


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AltomTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
