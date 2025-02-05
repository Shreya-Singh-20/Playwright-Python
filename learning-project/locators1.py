from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')


    #cssSelector - id - #, class - ., attribute tagname[attribute = "value"]

    page.wait_for_selector('input[name="username"]').fill("Admin")
    # username.type('Admin')
    password = page.wait_for_selector('input[type="password"]')
    password.type('admin123')
    login_button = page.wait_for_selector('button[type="submit"]')
    login_button.click()
    page.wait_for_timeout(3000)