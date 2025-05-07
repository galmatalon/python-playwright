import pytest
from playwright.sync_api import Page
from utils.config_reader import ConfigReader
from pages.wizard1_page import Wizard1Page
from pages.wizard2_page import Wizard2Page
from pages.wizard3_page import Wizard3Page


@pytest.fixture(scope="class")
def setup_page_class(request, browser):
    request.cls.page = browser.new_page()
    url = ConfigReader.read_config("global","url")
    request.cls.page.goto(url)
    request.cls.wizard1_page = Wizard1Page(request.cls.page)
    request.cls.wizard2_page = Wizard2Page(request.cls.page)
    request.cls.wizard3_page = Wizard3Page(request.cls.page)
    yield
    request.cls.page.close()
    browser.close()


@pytest.fixture(scope="function")
def setup_page_function(request, page: Page):
   # page.goto("https://galmatalon.github.io/tutorials/indexNoID.html")
    url = ConfigReader.read_config("global","url")
    page.goto(url)
    request.cls.wizard1_page = Wizard1Page(page)
    request.cls.wizard2_page = Wizard2Page(page)
    request.cls.wizard3_page = Wizard3Page(page)