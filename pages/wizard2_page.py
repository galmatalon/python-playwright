from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.components.header_area import HeaderArea
from pages.components.next_component import NextComponent


class Wizard2Page(HeaderArea, BasePage):
    def __init__(self, page:Page):
        super().__init__(page)
        self.__next = NextComponent(page)

    __BEGINNER_BTN = ".fa-blind"
    __INTERMEDIATE_BTN = ".fa-child"
    __ADVANCED_BTN = ".fa-star"
    __BACK_BTN = ".btn-previous"

    def choose_option(self, my_option):
        match my_option:
            case "beginner":
                self.click(self.__BEGINNER_BTN)
            case "intermediate":
                self.click(self.__INTERMEDIATE_BTN)
            case "advanced":
                self.click(self.__ADVANCED_BTN)
            case _:
                # Optional: handle unexpected options
                raise ValueError(f"Unsupported option: {my_option}")
        self.__next.next()

    def back(self):
        self.click(self.__BACK_BTN)
