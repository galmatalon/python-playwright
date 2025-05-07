import pytest
from tests.base_test import BaseTest


@pytest.mark.usefixtures("setup_page_function")
class Test2(BaseTest):
    def test_01_wizards(self, page):
        self.wizard1_page.fill_page("gal1", "mmmm1", "gal1@gmail.com")

    def test_02_wizards(self):
        self.wizard1_page.fill_page("gal1", "mmmm1", "gal1@gmail.com")
        self.wizard2_page.choose_option("advanced")
