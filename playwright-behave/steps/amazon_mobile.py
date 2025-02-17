import selectors
import pytest

from playwright.sync_api import sync_playwright
from behave import given, when, then


@pytest.fixture
@given("I click on the {bigtab} tab")
def click_mobile_tab(context, bigtab):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False, slow_mo=500)
    context.ctx = context.browser.new_context()
    context.page = context.ctx.new_page()
    url = "https://www.amazon.in/"
    context.page.goto(url, wait_until="domcontentloaded")
    context.page.wait_for_selector(
        f'//div[@id="nav-xshop"]//a[contains(text(), {bigtab})]'
    )
    context.page.click(f'//div[@id="nav-xshop"]//a[contains(text(), {bigtab})]')


@when("I hover on {subtab}")
def click_laptop_accessories(context, subtab):
    # context.page.wait_for_selector(f'//a/span[contains(text(), {subtab})]')
    context.page.wait_for_selector(f"//a/span[contains(text(), {subtab})]").hover()
    # context.page.click('//a[@aria-label="Laptops & Accessories, You are currently on a drop-down. To open this drop-down, Press Enter."]')


# //a[text()='Thin and light laptops']
@then("I click on {middletab} First product should be selected and added to cart")
def click_lenovo(context, middletab):
    context.page.wait_for_selector(f'//a[text()="{middletab}"]')
    context.page.click('f//a[text()="{middletab}"]')
    context.page.wait_for_timeout(5000)
    # context.page.get_by_text(
    #     "Lenovo Tab M10 FHD 3rd Gen| 10.1 Inch (25.65 cm) | 4 GB RAM, 64 GB ROM| Wi-Fi + LTE, Voice Calling | Full HD Display| Dual Speakers| Octa-Core Processor (Storm Grey)").scroll_into_view_if_needed()
    context.page.wait_for_selector(
        '//div[contains(@class, "apbSearchResultsContainer")]//div'
    ).click()
    print(context.ctx.pages)
    context.page = context.ctx.pages[1]
    context.page.wait_for_timeout(3000)
    context.page.wait_for_selector('//h1[@id="title"]')
    context.page.wait_for_selector(
        '//span[@id="submit.add-to-cart"]//input[@type="submit"]'
    ).scroll_into_view_if_needed()
    context.page.click('//span[@id="submit.add-to-cart"]//input[@type="submit"]')
    context.page.wait_for_selector(
        '//div[@id="attachDisplayAddBaseAlert"]//h4[contains(text(), "Added to cart")]'
    )
    context.page.click(
        "//input[@aria-labelledby='attach-sidesheet-checkout-button-announce']"
    )
    context.page.wait_for_selector('//h1[contains(text(), "Sign in")]')
    context.page.wait_for_timeout(6000)
    print("Product successfully added to cart")
