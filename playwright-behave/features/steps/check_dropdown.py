from behave import given, when, then


@given("User hovers on the language dropdown")
def user_hovers_dropdown(context):
    url = "https://www.amazon.in/"
    context.page.goto(url)
    context.page.wait_for_selector(
        '(//a[@id="icp-nav-flyout"]//span/following-sibling::span)[1]'
    ).hover()


@when("User clicks on change country region")
def user_clicks_change_country_region(context):
    context.page.wait_for_selector(
        '(//div[contains(text(), "Change country/region")])[1]'
    ).click()
    context.page.wait_for_selector('//h3[contains(text(), "Website (Country/Region)")]')


@when("Selects a country in which he wants to change the country")
def select_country(context):
    context.page.wait_for_selector('//span[@id="icp-dropdown"]').click()
    context.page.wait_for_selector(
        '//li//a[contains(text(), "United States")]'
    ).scroll_into_view_if_needed()
    context.page.wait_for_selector('//li//a[contains(text(), "United States")]').click()
    # context.page.wait_for_selector('//span[contains(text(), "Go to website")]').is_visible()
    # context.page.wait_for_selector('//span[contains(text(), "Go to website")]').click()
    context.page.wait_for_selector(
        "//input[@aria-labelledby='icp-save-button-announce']"
    ).click()
    context.page.wait_for_timeout(3000)


@then("The country flag is shown on the home page")
def check_country_flag(context):
    updated_flag = context.page.wait_for_selector(
        '//span[@class="nav-line-2"]//div'
    ).inner_text()
    assert "EN" in updated_flag, f"Expected 'EN' in location, but got '{updated_flag}'"
