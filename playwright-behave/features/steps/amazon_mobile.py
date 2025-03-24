import selectors
import pytest
import re

from playwright.sync_api import sync_playwright
from behave import given, when, then


@pytest.mark.usefixtures("click_mobile_tab")
@given("I click on the {bigtab} tab")
def click_mobile_tab(context, bigtab):
    # context.playwright = sync_playwright().start()
    # context.browser = context.playwright.chromium.launch(
    #     headless=False, slow_mo=500, args=["--start-maximized"]
    # )
    # context.ctx = context.browser.new_context(no_viewport=True)
    # context.page = context.ctx.new_page()
    url = "https://www.amazon.in/"
    context.page.goto(url, wait_until="domcontentloaded")
    assert (
        context.page.title()
        == "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in"
    )
    context.page.wait_for_selector(
        f'//div[@id="nav-xshop"]//a[contains(text(), {bigtab})]'
    )
    context.page.click(f'//div[@id="nav-xshop"]//a[contains(text(), {bigtab})]')


@when("I hover on {subtab}")
def click_laptop_accessories(context, subtab):
    # context.page.wait_for_selector(f'//a/span[contains(text(), {subtab})]')
    context.page.wait_for_selector(f"//a/span[contains(text(), {subtab})]").click()
    # context.pge.click('//a[@aria-label="Laptops & Accessories, You are currently on a drop-down. To open this drop-down, Press Enter."]')


# //a[text()='Thin and light laptops']
# //div[@id='s-refinements']//div[4]//div//span[contains(text(), 'Samsung')]
@then("I click on {middletab} First product should be selected and added to cart")
def click_lenovo(context, middletab):
    print(
        f"waiting for :   //div[@id='s-refinements']//div[4]//input[@aria-labelledby={middletab}]/following-sibling::i"
    )
    context.page.wait_for_selector(
        f"//div[@id='s-refinements']//div[4]//input[@aria-labelledby={middletab}]/following-sibling::i"
    ).scroll_into_view_if_needed()

    context.page.locator(
        f"//div[@id='s-refinements']//div[4]//input[@aria-labelledby={middletab}]/following-sibling::i"
    ).click()
    # context.page.wait_for_timeout(5000)
    # context.page.get_by_text(
    #     "Lenovo Tab M10 FHD 3rd Gen| 10.1 Inch (25.65 cm) | 4 GB RAM, 64 GB ROM| Wi-Fi + LTE, Voice Calling | Full HD Display| Dual Speakers| Octa-Core Processor (Storm Grey)").scroll_into_view_if_needed()
    context.page.wait_for_selector(
        '//div[contains(@class, "a-section a-spacing-base")]//div'
    ).click()
    # first_product = context.page.locator(
    #     '//div[contains(@class, "s-result-item")][1]//a[contains(@class, "a-link-normal")]')
    # first_product.scroll_into_view_if_needed()
    # first_product.click()

    # print(context.ctx.pages)
    context.page.wait_for_timeout(5000)
    context.page = context.ctx.pages[1]
    product_price = context.page.locator(
        '//div[@id="apex_desktop"]//span//span[@class="a-price-whole"]'
    ).inner_text()
    product_price = product_price.replace(",", "").strip()
    context.page.wait_for_selector('//h1[@id="title"]')
    context.page.wait_for_selector(
        '//span[@id="submit.add-to-cart"]//input[@type="submit"]'
    ).scroll_into_view_if_needed()
    # context.page.click('//span[@id="submit.add-to-cart"]//input[@type="submit"]')
    add_to_cart = '//span[@id="submit.add-to-cart"]//input[@type="submit"]'
    context.page.click(add_to_cart)
    # assert context.page.locator("//div//h1[contains(text(), 'Added to cart')]").is_visible() == True
    print("Item is added to cart.")
    # context.page.wait_for_selector(
    #     '//div[@id="attachDisplayAddBaseAlert"]//h4[contains(text(), "Added to cart")]'
    # )
    # context.page.wait_for_selector('//div[contains(@class, "sc-added-item")]')

    if context.page.locator("//a[@id='attach-close_sideSheet-link']").is_visible():
        context.page.click("//a[@id='attach-close_sideSheet-link']")
    context.page.click("//div[@id='nav-cart-count-container']")
    # cart = "//div[@id='nav-cart-count-container']"
    # context.page.click(cart)
    # cart_count = context.page.locator('//span[@id="nav-cart-count"]').inner_text().strip()
    # if cart_count == "0":
    #     print("Cart is empty, product may not have been added successfully.")

    cart_price = context.page.locator(
        '//span[@id="sc-subtotal-amount-activecart"]'
    ).inner_text()
    cart_price = cart_price.replace(",", "").strip()
    cart_price = re.sub(r"[^\d.]", "", cart_price)
    if float(product_price) == float(cart_price):
        print("Prices match")
        context.page.wait_for_selector('//span[@id="sc-buy-box-ptc-button"]').click()
    context.page.wait_for_selector('//h1[contains(text(), "Sign in")]')
    # context.page.wait_for_timeout(6000)
    print("Product successfully added to cart")
    # context.ctx.close()
    # context.browser.close()
    # context.playwright.stop()
