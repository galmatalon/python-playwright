from playwright.sync_api import Page

from pages.base_page import BasePage


class HeaderArea(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    __ABOUT_BTN = ".nav-pills>li:nth-child(1)"
    __ACCOUNT_BTN = ".nav-pills>li:nth-child(2)"
    __ADDRESS_BTN = ".nav-pills>li:nth-child(3)"

    def option_about(self):
        self.click(self.__ABOUT_BTN)

    def option_account(self):
        self.click(self.__ACCOUNT_BTN)

    def option_address(self):
        self.click(self.__ADDRESS_BTN)