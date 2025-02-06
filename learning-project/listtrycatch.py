from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    try:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto('https://demo.automationtesting.in/Selectable.html')

        #Store multiple elements using list
        elements = page.query_selector_all('a')

        print(len(elements))
        for i in elements:
            # print(i.text_content())
            print(i.get_attribute('href'))

        page.wait_for_timeout(2000)

    except Exception as e:
        print(str(e))
    finally:
        print('Execute')