from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto('https://demo.automationtesting.in/Selectable.html')
    #Mouse Actions
    #Hover the dropdown
    page.wait_for_selector('//a[text()="SwitchTo"]').hover()

    #Click on the element
    page.wait_for_selector('//a[text()="SwitchTo"]').click()

    #Double click
    page.wait_for_selector('//a[text()="SwitchTo"]').dblclick()

    #Right on element
    page.wait_for_selector('//a[text()="SwitchTo"]').click(button="right")

    #Shift Click
    page.wait_for_selector('//a[text()="SwitchTo"]').click(modifiers=["Shift"])


    #Keyboard Actions
    page.wait_for_selector('//a[text()="SwitchTo"]').press("A")
    #A-Z, 0-9, F1-F12, All special character, ArrowRight, ArrowDown, PageUp, Enter, Control, Command
    page.wait_for_selector('//a[text()="SwitchTo"]').press("$")


    page.wait_for_timeout(2000)