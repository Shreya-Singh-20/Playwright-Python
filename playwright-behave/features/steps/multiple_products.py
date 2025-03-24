from behave import given, when, then
from playwright.sync_api import sync_playwright


@given("I click on the search box of amazon")
def navigate(context):
    # context.playwright = sync_playwright().start()
    # context.browser = context.playwright.chromium.launch(headless=False, slow_mo=500)
    # context.ctx = context.browser.new_context()
    # context.page = context.ctx.new_page()
    url = "https://www.amazon.in/"
    context.page.goto(url, wait_until="load")


@when("I enter the following product names and add them to the cart")
def enter_product(context):
    # while name:
    #     context.page.fill('//input[@id="twotabsearchtextbox"]', name)
    #     context.page.click("//span[@id='nav-search-submit-text']//input[@type='submit']")
    #     context.page.wait_for_selector('//div[@data-csa-c-pos="1"]//div[@data-cy="asin-faceout-container"]')
    #     context.page.click('//div[@data-csa-c-pos="1"]//div[@data-cy="asin-faceout-container"]')
    #     context.page.wait_for_selector('//h1[@id="title"]')
    #     context.page.wait_for_selector('//div[@id="addToCart_feature_div"]//input[@name="submit.add-to-cart"]').scroll_into_view_if_needed()
    #     context.page.click('//div[@id="addToCart_feature_div"]//input[@name="submit.add-to-cart"]')
    #     if context.page.locator("//a[@id='attach-close_sideSheet-link']").is_visible():
    #         context.page.click("//a[@id='attach-close_sideSheet-link']")
    #     # context.page.click("//div[@id='nav-cart-count-container']")
    #     # context.page.fill('//input[@id="twotabsearchtextbox"]', name)

    context.page_counter = 0
    for column in context.table:
        product_name = column[0]
        context.page.fill('//input[@id="twotabsearchtextbox"]', product_name)
        # context.page.keyboard.press('Enter')
        context.page.click(
            "//span[@id='nav-search-submit-text']//input[@type='submit']"
        )
        # context.page.wait_for_selector('//div[@data-csa-c-pos="1"]//div[@data-cy="asin-faceout-container"]')
        #
        context.page.click("(//div[@data-cy='title-recipe'])[1]")
        context.page_counter += 1
        context.page.wait_for_timeout(5000)
        print(
            "-------------- Going for page "
            + str(context.page_counter)
            + "-------------------------"
        )
        # context.page.locator('//div[@data-csa-c-pos="1"]//div[@data-cy="asin-faceout-container"]').click()
        context.page = context.ctx.pages[context.page_counter]
        #
        # context.page.wait_for_selector('//h1[@id="title"]')
        #
        # button_number = 2 ? context.page_counter = 1
        add_to_cart = "(//input[@id='add-to-cart-button'])[1]"
        # context.page.wait_for_selector(add_to_cart).scroll_into_view_if_needed()
        # context.page.wait_for_selector(add_to_cart).click()
        if context.page.locator(add_to_cart).is_visible():
            context.page.click(add_to_cart)
        else:
            print(f"Add to Cart button not found for {product_name}, skipping.")

        # context.page.get_by_role("button", name="Add to Cart", exact=True)
        side_sheet_close = "//a[@id='attach-close_sideSheet-link']"
        try:
            if context.page.locator(side_sheet_close).is_visible():
                context.page.click(side_sheet_close)

        except:
            pass


@then("I verify that all products are in the cart")
def verify_cart(context):
    context.page = context.ctx.pages[0]
    context.page.click("//div[@id='nav-cart-count-container']")


@then("I proceed to checkout")
def checkout(context):
    context.page.click("//input[@name='proceedToRetailCheckout']")
    context.page.wait_for_selector('//h1[contains(text(), "Sign in")]')
    context.page.wait_for_timeout(1000)
    print("Checked out")
    # context.ctx.close()
    # context.browser.close()
    # context.playwright.stop()
