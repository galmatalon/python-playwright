import pytest
from tests.base_test import BaseTest
from data.test_data import TestData

@pytest.mark.usefixtures("setup_page_function")
class Test2(BaseTest):

    users_data = [("gal1", "m1", "gal1@gmail.com"),
                  ("gal2", "m2", "gal2@gmail.com")]

    @pytest.mark.parametrize("first_name, last_name, email", users_data)
    def test_01_wizards(self, first_name, last_name, email):
        self.wizard1_page.fill_page(first_name, last_name, email)

    def test_02(self):
        pass
