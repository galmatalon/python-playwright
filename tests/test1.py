import pytest
from playwright.sync_api import sync_playwright

from pages.wizard1_page import Wizard1Page
from pages.wizard2_page import Wizard2Page
from pages.wizard3_page import Wizard3Page
from tests.base_test import BaseTest


@pytest.mark.usefixtures("setup_page_class")
class Test1(BaseTest):

    def test_01_wizards(self):
        self.wizard1_page.fill_page("Gal","Matalon","gal@gmail.com")
        self.wizard1_page.option_about()

    def test_02_wizards(self):
        self.wizard2_page.choose_option("beginner")

    def test_03_wizards(self):
        self.wizard3_page.fill_page("Dudu", "1", "Netanya", "Italy")


