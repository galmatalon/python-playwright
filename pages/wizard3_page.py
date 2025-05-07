from pages.base_page import BasePage
from pages.components.header_area import HeaderArea


class Wizard3Page(HeaderArea, BasePage):
    def __init__(self, page):
        super().__init__(page)

    __STREET_NAME_FIELD = "[name='streetname']"
    __STREET_NUMBER_FIELD = "[name='streetnumber']"
    __CITY_FIELD = "[name='city']"
    __COUNTRY_DD = "#country"
    __FINISH_BTN = "#finish"

    def fill_page(self, street, number, city, country):
        self.fill_text(self.__STREET_NAME_FIELD, street)
        self.fill_text(self.__STREET_NUMBER_FIELD, number)
        self.fill_text(self.__CITY_FIELD, city)
        self.select_option(self.__COUNTRY_DD, country)
        self.click(self.__FINISH_BTN)
