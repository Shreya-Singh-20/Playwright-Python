import asyncio
from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=3000)
        page = await browser.new_page()
        await page.goto("https://playwright.dev/python")
        await page.screenshot(path="./screenshot.png")
        await browser.close()


asyncio.run(main())
# await main()
