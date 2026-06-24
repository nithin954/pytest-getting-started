import pytest
from playwright.sync_api import Playwright


@pytest.fixture(params=["Chrome", "Firefox"], scope="class")
def init_browser(request, playwright: Playwright):
    if request.param == "Chrome":
        browser = playwright.chromium.launch(headless=False)
    if request.param == "Firefox":
        browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com")

    request.cls.page = page
    yield page

    page.close()
    context.close()
    browser.close()
