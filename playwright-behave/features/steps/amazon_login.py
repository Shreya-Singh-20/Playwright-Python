import allure
from allure_commons.types import AttachmentType
from datetime import datetime
from playwright.sync_api import Playwright, sync_playwright
from behave import given, when, then


@given("User visits amazon.in")
def step_login_amazon(context):
    context.page.goto("https://amazon.in")


@then("User goes to login page")
def user_go_to_login(context):
    context.page.click('//span[contains(text(), "Account & Lists")]')


@when("User enters mobile number and click continue")
def user_go_to_login(context):
    context.page.locator("//input[@name='email']").press_sequentially(
        "+917607745307", delay=200
    )
    context.page.click("//input[@type='submit']")


@when("User enters password and click continue")
def user_go_to_login(context):
    if context.page.locator('//div[@id="otp_box_label"]').is_visible():
        context.page.wait_for_timeout(15000)
    else:
        context.page.locator('//input[@type="password"]').press_sequentially(
            "Password123", delay=200
        )
        context.page.click('//input[@id="signInSubmit"]')


@then("User should be on homepage")
def user_validates_home(context):
    path = f"reports/screenshots/{str(datetime.now()).replace('-','').replace(' ', '').replace(':', '')}.png"
    ss = context.page.screenshot(path=path)
    allure.attach(
        ss, name="Home PAge Screenshot", attachment_type=allure.attachment_type.PNG
    )


#
# @when("User enters valid details in all sections")
# def step_enter_valid_details(context):
#     context.page.wait_for_selector('//a[@id="nav-logo-sprites"]')
#     context.page.click('//a[@data-csa-c-content-id="nav_ya_signin"]')
#     context.page.wait_for_selector('//h1[contains(text(), "Sign in")]')
#     context.page.locator('//input[@id="ap_email"]').press_sequentially('7607745307', delay=200)
#     context.page.click('//input[@type="submit"]')
#     context.page.wait_for_selector('//h1[contains(text(), "Looks like you are new to Amazon")]')
#     context.page.click('//span[@id="intention-submit-button"]')
#     context.page.wait_for_selector('//h1[contains(text(), "Create Account")]')
#     context.page.locator('//input[@id="ap_customer_name"]').press_sequentially("Shreya Singh", delay=200)
#     context.page.locator('//input[@id="ap_password"]').press_sequentially('password1234', delay=200)
#     context.page.click('//input[@id="continue"]')
#     if context.page.locator('//div[@id="otp_box_label"]').is_visible():
#         context.page.wait_for_timeout(15000)
#
#     context.page.wait_for_timeout(20000)
#
#     if context.page.locator('//div[@id="otp_box_label"]').is_visible():
#         context.page.wait_for_timeout(15000)
#
# @then("User should be seeing the Amazon homepage for that user")
# def step_login_amazon_homepage(context):
#     context.page.wait_for_selector('//a[@id="nav-logo-sprites"]')
#     context.path = context.page.video.path()
#     allure.attach.file(context.path, name="amazon-register", attachment_type=AttachmentType.MP4)
#     context.page.wait_for_timeout(10000)
#     print("New user registered")
#     context.ctx.close()
#     context.browser.close()
#     context.playwright.stop()
