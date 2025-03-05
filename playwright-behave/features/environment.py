from playwright.sync_api import sync_playwright
import allure


def before_all(context):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(
        headless=False, args=["--start-maximized"], slow_mo=500
    )


def before_scenario(context, scenario):
    context.ctx = context.browser.new_context(
        no_viewport=True, record_video_dir="reports/video"
    )
    context.page = context.ctx.new_page()


def after_scenario(context, scenario):
    context.page.wait_for_timeout(30000)
    context.page.close()
    path = context.page.video.path()
    allure.attach.file(path, name=f"Video", attachment_type=allure.attachment_type.MP4)
    context.ctx.close()


def after_all(context):
    context.browser.close()
    context.playwright.stop()
