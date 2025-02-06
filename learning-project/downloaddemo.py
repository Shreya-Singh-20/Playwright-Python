from playwright.sync_api import sync_playwright


def download_handle(download):
    location_file = './files/test.zip'
    download.save_as(location_file)
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://demo.imacros.net/Automate/Downloads', wait_until='load')
    page.on('download', download_handle())

    page.wait_for_selector('//a[@href="/Content/Download.zip"]').click()
    page.wait_for_timeout(3000)