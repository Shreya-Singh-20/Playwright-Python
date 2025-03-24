from behave import given, when, then


@given("User is on the home page")
def home_page(context):
    url = "https://www.amazon.in/"
    context.page.goto(url)


@when("User enters the new location")
def new_location(context):
    context.page.wait_for_selector(
        '//a[@id="nav-global-location-popover-link"]'
    ).click()
    context.page.wait_for_selector('//h4[contains(text(), "Choose your location")]')
    context.page.wait_for_selector('//input[@autocomplete="postal-code"]').fill(
        "302026"
    )
    context.page.wait_for_selector(
        '//span[@id="GLUXZipUpdate"]//input[@type="submit"]'
    ).click()
    context.page.wait_for_timeout(3000)


@then("The location must be updated")
def location_updated(context):
    context.page.wait_for_timeout(1000)
