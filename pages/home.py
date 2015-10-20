from selenium.webdriver.common.by import By
from element import Element
from page import Page


class Home(Page):
    def __init__(self, driver):
        Page.__init__(self, driver)
        self.altom_logo = Element(self.driver, (By.XPATH, ".//*[@id='site-title']/a/img"))
        self.sidebar = Element(self.driver, (By.CLASS_NAME, "sidebar"))
        self.main_content = Element(self.driver, (By.ID, "mainContent"))
        self.main_menu = Element(self.driver, (By.ID, "mainMenu"))
        self.video = Element(self.driver, (By.ID, "presentation"))
        self.phone_number = Element(self.driver, (By.CLASS_NAME, "mainPhone"))
        self.blocks = Element(self.driver, (By.CLASS_NAME, "blocks"))

    def is_displayed(self):
        self.altom_logo.is_displayed()
        self.sidebar.is_displayed()
        self.main_content.is_displayed()
        self.main_menu.is_displayed()
        self.video.is_displayed()
        self.phone_number.is_displayed()
        self.blocks.is_displayed()
        return True
