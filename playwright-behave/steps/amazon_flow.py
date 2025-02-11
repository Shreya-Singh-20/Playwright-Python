from behave import given, when, then
from playwright.sync_api import sync_playwright


@given("I click on the search box")
def navigate(context):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False, slow_mo=500)
    context.ctx = context.browser.new_context()
    context.page = context.ctx.new_page()
    url = "https://www.amazon.in/"
    context.page.goto(url)


# Scenario 1: Product desired by user exists


@when("I enter the product details")
def enter_correct_details(context):
    context.page.fill('//input[@placeholder="Search Amazon.in"]', "oneplus 13r")
    context.page.click('//input[@id="nav-search-submit-button"]')


@then("The product details are provided")
def prod_details(context):
    context.page.wait_for_timeout(3000)
    context.browser.close()
    context.playwright.stop()


# Scenario 2: Product desired by user does not exists


@when("I enter the details of a product")
def enter_details_not_exist(context):
    context.page.fill(
        '//input[@placeholder="Search Amazon.in"]',
        "ccccccccccccccccccccccccccccccccccccccccccccccccc",
    )
    context.page.click('//input[@id="nav-search-submit-button"]')


@then("It should give me an error message")
def error_message(context):
    context.page.wait_for_selector(
        '//span[contains(text(), "No results for")]/following-sibling::span'
    )
    context.page.wait_for_timeout(3000)
    context.browser.close()
    context.playwright.stop()


# Scenario 3: A product is added to cart


@when("I enter the product details and select it")
def enter_details(context):
    context.page.fill('//input[@placeholder="Search Amazon.in"]', "iphone 16pro max")
    context.page.click('//input[@id="nav-search-submit-button"]')
    (
        context.page.locator(
            "//span[contains(text(), "
            '"iPhone 16 Pro Max 1 TB: 5G Mobile Phone with Camera Control, '
            "4K 120 fps Dolby Vision and a Huge Leap in Battery Life. "
            'Works with AirPods; Natural Titanium")]'
        ).scroll_into_view_if_needed()
    )
    context.page.click(
        "//span[contains(text(), "
        '"iPhone 16 Pro Max 1 TB: 5G Mobile Phone with Camera Control, '
        "4K 120 fps Dolby Vision and a Huge Leap in Battery Life. "
        'Works with AirPods; Natural Titanium")]'
    )
    print(context.ctx.pages)
    context.page = context.ctx.pages[1]


@then("The product is added to cart")
def add_to_cart(context):
    context.page.click("(//input[@id='add-to-cart-button'])[2]")
    context.page.wait_for_selector('//h1[contains(text(), "Added to cart")]')
    context.page.click("//span[@id='sw-gtc']//a")
    context.page.wait_for_selector(
        '//input[@data-feature-id="proceed-to-checkout-action"]'
    )
    context.page.wait_for_timeout(3000)
    context.browser.close()
    context.playwright.stop()


# # Scenario 4: To checkout products
# @given("The product is added to cart")
# def checkout_cart(context):
