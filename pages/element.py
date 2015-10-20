from selenium.common.exceptions import NoSuchElementException


class Element(object):
    """
    Base class for all elements.
    """

    driver = None
    default_implicit_wait = 10
    locator = None

    def __init__(self, driver, locator):
        """
        Constructor
        """
        self.driver = driver
        self.locator = locator

    def is_displayed(self):
        self.driver.find_element(*self.locator)
        print "element %s is displayed" % str(self.locator)

    @property
    def displayed_now(self):
        """
        checks if element is displayed but won't assert
        :return:
         true: if found
         false: if not found
        """
        self.driver.implicitly_wait(0)
        try:
            self.driver.find_element(*self.locator)
            print "element %s is present" % str(self.locator)
            return True
        except NoSuchElementException:
            print "element %s is NOT present" % str(self.locator)
            return False
        finally:
            self.driver.implicitly_wait(self.default_implicit_wait)

    def click(self):
        print "clicking on %s" % str(self.locator)
        self.driver.find_element(*self.locator).click()

    def send_keys(self, text):
        print "entering %s on %s" % (text, str(self.locator))
        self.driver.find_element(*self.locator).send_keys(text)

    def clear_text(self):
        print "clearing text on field %s" % str(self.locator)
        self.driver.find_element(*self.locator).clear()
