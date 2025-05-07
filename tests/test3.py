import pytest
from tests.base_test import BaseTest

@pytest.mark.usefixtures("setup_page_function")
class Test2(BaseTest):

    @pytest.mark.parametrize("user, last_name, email", GlobalData.users_data)
    def test_01_wizards(self, user, last_name, email):
        self.wizard1_page.fill_page(user, last_name, email)

