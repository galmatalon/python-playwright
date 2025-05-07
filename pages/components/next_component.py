from playwright.sync_api import Page

from pages.base_page import BasePage


class NextComponent(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    __NEXT_BTN = ".btn-next"

    def next(self):
        self.click(self.__NEXT_BTN)