import pytest
from selenium import webdriver


@pytest.fixture()
def browser():
    chrome_browser = webdriver.Chrome()
    return chrome_browser