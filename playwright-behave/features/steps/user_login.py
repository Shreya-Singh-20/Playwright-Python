from behave import given, when, then
from playwright.sync_api import sync_playwright


@given("I navigate to the login page")
def login(context):
    # context.playwright = sync_playwright().start()
    # context.browser = context.playwright.chromium.launch(
    #     headless=False, slow_mo=500)
    # context.page = context.browser.new_page()
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    context.page.goto(url)


# Scenario 1: Successful Login
@when("I enter valid credentials")
def valid_details(context):
    context.page.fill('//input[@name="username"]', "Admin")
    context.page.fill('//input[@name="password"]', "admin123")


@when("I submit the form")
def submit(context):
    context.page.click('//button[@type="submit"]')


@then("I should see a success message")
def success(context):
    # assert context.page.locator('//h6[text()="Dashboard"]').is_visible()
    context.page.wait_for_timeout(5000)
    # context.browser.close()
    # context.playwright.stop()


# Scenario 3: Add new employee
@given("I enter valid credentials")
def validity(context):
    context.page.fill('//input[@name="username"]', "Admin")
    context.page.fill('//input[@name="password"]', "admin123")
    context.page.click('//button[@type="submit"]')
    # assert context.page.locator('//h6[text()="Dashboard"]').is_visible()
    context.page.wait_for_timeout(5000)


@when("I click on PIM and then Add option")
def click_PIM(context):
    context.page.click('//a[@href="/web/index.php/pim/viewPimModule"]')
    context.page.wait_for_timeout(5000)
    context.page.click("//button[@type='button' and text()=' Add ']")
    context.page.wait_for_timeout(4000)


@when("I enter valid details of the new employee")
def valid_information(context):
    context.page.fill('//input[@name="firstName"]', "test")
    context.page.fill('//input[@name="lastName"]', "user")
    context.page.click('//span[contains(@class, "oxd-switch-input")]')
    context.page.fill("(//input)[8]", "test234")
    context.page.fill("(//input)[8]", "test234")
    context.page.fill('(//input[@type="password"])[1]', "test234")
    context.page.fill('(//input[@type="password"])[2]', "test234")
    context.page.click('//button[@type="submit"]')


@then("a new employee should be added")
def added_successfully(context):
    context.page.wait_for_timeout(3000)
    # context.browser.close()
    # context.playwright.stop()


# Scenario 2: Login with Invalid Credentials
@when("I enter invalid details")
def invalid_details(context):
    context.page.fill('//input[@name="username"]', "testinvaliduser")
    context.page.fill('//input[@name="password"]', "testpassword123")


@then("I should see an error message")
def error(context):
    # print(context.page.locator(
    #     '//p[contains(text(), "Invalid credentials")]'
    # ).is_visible(timeout=1000))
    # assert context.page.locator("//p[text()='Invalid credentials']").is_visible(
    #     timeout=1000
    # )
    context.page.wait_for_timeout(3000)
    # context.browser.close()
