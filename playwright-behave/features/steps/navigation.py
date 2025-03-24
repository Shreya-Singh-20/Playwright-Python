from playwright.sync_api import sync_playwright
from behave import given, when, then


@given("I open the Amazon website")
def step_open_amazon(context):
    # context.playwright = sync_playwright().start()
    # context.browser = context.playwright.chromium.launch(headless=False, args=["--start-maximized"])
    # context.ctx = context.browser.new_context(no_viewport=True)
    # context.page = context.ctx.new_page()
    context.page.goto("https://www.amazon.in", wait_until="load")


@when('I click on "{menu_option}" from the header')
def step_click_menu(context, menu_option):
    # xpath = menu_xpath.get(menu_option)
    xpath = f"(//div[@id='nav-xshop']//a[contains(text(), '{menu_option}')])[1]"
    if not xpath:
        raise ValueError(
            f"Menu option '{menu_option}' not found in menu_xpath dictionary"
        )

    context.page.locator(xpath).click()


@then('I should be navigated to the "{expected_page}"')
def step_verify_navigation(context, expected_page):
    context.page.wait_for_load_state("domcontentloaded")
    print("Expected URL:", expected_page)
    current_url = context.page.url
    print("Current URL:", current_url)

    assert (
        expected_page in current_url
    ), f"Expected {expected_page}, but got {current_url}"

    # Close browser
    # context.page.close()
    # context.ctx.close()
    # context.browser.close()
    # context.playwright.stop()
