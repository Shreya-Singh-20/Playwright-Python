from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://demo.automationtesting.in/FileUpload.html')

    file_upload = './text.txt'

    upload_location = page.query_selector('//input[@id="input-4"]')


    #TO UPLOAD THE FILE
    upload_location.set_input_files(file_upload)
    page.wait_for_timeout(3000)