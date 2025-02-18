import behave
from behave import fixture, given, when, then
from playwright.async_api import async_playwright, expect


@fixture
async def browser_fixture(context):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context.browser = browser
        context.page = await context.new_page()
        yield context.page
        await context.page.close()
        await context.browser.close()


@given("user goes to google")
async def go_to_google(context):
    page = context.page
    await page.goto("https://google.com")
    await page.wait_for_timeout(3000)
    title = await page.title()
    assert "Google" in title
