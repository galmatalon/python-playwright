import pytest
from tests.base_test import BaseTest
from data.global_data import GlobalData


@pytest.mark.usefixtures("setup_page_function")
class Test2(BaseTest):

    @pytest.mark.parametrize("user, last, email", GlobalData.users_data)
    def test_01_wizards(self, user, last, email):
        self.wizard1_page.fill_page(user, last, email)



