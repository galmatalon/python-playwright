from tests.base_test import BaseTest


class TestPage2(BaseTest):

    def test_01_choose_beginner(self):
        self.wizard1_page.fill_page("Gal", "Matalon", "gal@gmail.com")
        self.wizard2_page.choose_option("beginner")
