import pytest
from playwright.sync_api import expect

# @pytest.fixture(params=['Chrome', 'Firefox'], scope='class')
# def init_browser(request, playwright:Playwright):
#     if request.param == 'Chrome':
#         browser = playwright.chromium.launch(headless=False)
#     if request.param == 'Firefox':
#         browser = playwright.firefox.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://www.google.com")

#     request.cls.page = page
#     yield page

#     page.close()
#     context.close()
#     browser.close()


@pytest.mark.usefixtures("init_browser")
class TestGoogle:
    def test_title(self):
        expect(self.page).to_have_title("Google")  # type: ignore

    def test_url(self):
        expect(self.page).to_have_url("https://www.google.com/")  # type: ignore
