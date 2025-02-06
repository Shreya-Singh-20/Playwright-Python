import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    page=browser.new_page()
    yield page
    page.close()


def test_go_to_google(page):
    page.goto('https://www.google.com/', wait_until = 'load')
    assert 'Google' == page.title()


def test_go_to_redbus(page):
    page.goto('https://www.redbus.in/', wait_until = 'load')
    assert 'Bus Ticket Booking Online made Easy, Secure with Top Bus Operators - redBus' == page.title()