from playwright.sync_api import sync_playwright, Page, expect
from behave import given, when, then


MENU_XPATHS = {
    "All": "//a[@id='nav-hamburger-menu']",
    "Fresh": "//a[@data-csa-c-content-id='nav_cs_fresh']",
    "MX Player": "//a[@data-csa-c-slot-id='nav_cs_1']",
    "Sell": "//a[@data-csa-c-slot-id='nav_cs_2']",
    "Best Sellers": "//a[@data-csa-c-slot-id='nav_cs_3']",
    "Mobiles": "//a[@data-csa-c-slot-id='nav_cs_4']",
    "Today's Deals": "//a[@data-csa-c-slot-id='nav_cs_5']",
    "Customer Service": "//a[@data-csa-c-slot-id='nav_cs_6']",
    "Electronics": "//a[@data-csa-c-slot-id='nav_cs_7']",
    "Amazon Pay": "//a[@data-csa-c-slot-id='nav_cs_8']",
    "Prime": "//a[@data-csa-c-slot-id='nav_cs_9']",
    "New Releases": "//a[@data-csa-c-slot-id='nav_cs_10']",
    "Home & Kitchen": "//a[@data-csa-c-slot-id='nav_cs_11']",
}


@given("I open the Amazon website")
def step_open_amazon(context):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(
        headless=False, args=["--start-maximized"]
    )
    context.ctx = context.browser.new_context(no_viewport=True)
    context.page = context.browser.new_page()
    context.page.goto("https://www.amazon.in")


@when('I click on "{menu_option}" from the header')
def step_click_menu(context, menu_option):
    page: Page = context.page
    xpath = MENU_XPATHS.get(menu_option)

    if not xpath:
        raise ValueError(f"Menu option '{menu_option}' not found in MENU_XPATHS")
    context.page.locator(xpath).click()
    # if menu_option == "All":
    #     sidebar_xpath = "(//div[@id='hmenu-canvas'])[1]"
    #     try:
    #         expect((context.page.locator(sidebar_xpath).first)).to_be_visible()
    #     except(Exception):
    #         print("Got an exception : ", Exception)


@then('I should be navigated to the "{expected_page}"')
def step_verify_navigation(context, expected_page):
    context.page.wait_for_load_state("domcontentloaded")
    print("Expected URL : ", expected_page)
    current_url = context.page.url
    print(f"current_url: {current_url}")
    assert (
        expected_page in current_url
    ), f"Expected {expected_page}, but got {current_url}"

    # Close browser
    context.browser.close()
    context.playwright.stop()
