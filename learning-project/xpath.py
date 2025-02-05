from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

    #xpath-Relative xpath
    #using attribute - //tagname[@attributename="value"]

    # username_element=page.wait_for_selector('//input[@name="username"]')
    # username_element.type('Admin')
    # password_element=page.wait_for_selector('//input[@placeholder="Password"]')
    # password_element.type('admin123')
    # login_element=page.wait_for_selector('//button[@type="submit"]')
    # login_element.click()
    

    #text - //tagname[text()="text"]
    page.wait_for_selector('//p[text()="Forgot your password? "]').click()


    #contains
    #attributes - //tagname[contains(@attribute,"value")]
    #text - //tagname[contains(text(),"Forgot you password? ")]
    page.wait_for_timeout(3000)




    #dynamic - shreya123, shreya34567, shreya8901
    #starts-with - //tagname[starts-with(@id, 'shreya')]
    #ends-with - 234user


    #family
    #parent - //tagname[@id = "xy"]/parent::input[]
    #child - //tagname[@id = "xy"]/child::input[]
    #ancestor - 
    #sibling - //td[text()="Microsoft"]//following-sibling::td[2]
