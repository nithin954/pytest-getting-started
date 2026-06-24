from playwright.sync_api import Playwright, expect
import pytest


@pytest.fixture(scope="class")
def init_browser(request, playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com")

    # Store page in class
    request.cls.page = page

    yield

    page.close()
    context.close()
    browser.close()


@pytest.mark.usefixtures("init_browser")
class TestGoogle:
    def test_title(self):
        expect(self.page).to_have_title("Google")  # type: ignore

    def test_url(self):
        expect(self.page).to_have_url("https://www.google.com/")  # type: ignore
