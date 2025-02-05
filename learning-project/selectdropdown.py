from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://demo.automationtesting.in/Register.html')

    #Select Drop
    #1. Find the select location
    #select_dropdown = page.query_selector('//select[@id="Skills"]')
    #2. Select the option
    #select_dropdown.select_option(label='Art Design')
    page.select_option('//select[@id="Skills"]',label='AutoCAD')
    page.wait_for_timeout(5000)
