from playwright.sync_api import sync_playwright
from features.pages.app_page import AppPage


def before_all(context):
    headless = context.config.userdata.getbool("headless", False)
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=headless)

def before_scenario(context, scenario):
    context.page = context.browser.new_page()
    context.page.set_default_timeout(3000)
    context.app_page = AppPage(context.page)

def after_scenario(context, scenario):
    context.page.close()

def after_all(context):
    context.browser.close()
    context.playwright.stop()