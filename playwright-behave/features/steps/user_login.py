from behave import given, when, then
from playwright.sync_api import sync_playwright


@given("I navigate to the login page")
def login(context):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)
    context.page = context.browser.new_page()
    context.page.goto(
        "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    )


# Scenario 1: Successful Login
@when("I enter valid details")
def valid_details(context):
    context.page.fill('//input[@name="username"]', "Admin")
    context.page.fill('//input[@name="password"]', "admin123")


@when("I submit the form")
def submit(context):
    context.page.click('//button[@type="submit"]')


@then("I should see a success message")
def success(context):
    assert context.page.locator('//h6[text()="Dashboard"]').is_visible()
    context.page.wait_for_timeout(3000)
    context.browser.close()
    context.playwright.stop()


# Scenario 2: Login with Invalid Credentials
@when("I enter the invalid details")
def invalid_details(context):
    context.page.fill('//input[@name="username"]', "testinvaliduser")
    context.page.fill('//input[@name="password"]', "testpassword123")


@then("I should see an error message")
def error(context):
    assert context.page.locator(
        '//p[contains(text(), "Invalid credentials")]'
    ).is_visible()
    context.page.wait_for_timeout(3000)
    context.browser.close()
    context.playwright.stop()
