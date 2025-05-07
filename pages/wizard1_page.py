from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.components.next_component import NextComponent
from pages.components.header_area import HeaderArea
class Wizard1Page(HeaderArea, BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.__next = NextComponent(page)

    __FIRST_NAME_FIELD = "#firstname"
    __LAST_NAME_FIELD = "#lastname"
    __EMAIL_FIELD = "#email"


    def fill_page(self, first_name, last_name, email):
        self.fill_text(self.__FIRST_NAME_FIELD, first_name)
        self.fill_text(self.__LAST_NAME_FIELD, last_name)
        self.fill_text(self.__EMAIL_FIELD, email)
        self.__next.next()




