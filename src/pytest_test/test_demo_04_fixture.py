from playwright.sync_api import Playwright, expect
import pytest


@pytest.fixture(scope="module")
def setUp(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com/")

    yield page

    page.close()
    context.close()
    browser.close()


@pytest.mark.skip
def test_title(setUp):
    expect(setUp).to_have_title("Google")


@pytest.mark.skip
def test_url(setUp):
    expect(setUp).to_have_url("https://www.google.com/")


@pytest.fixture
def init(playwright: Playwright):
    print("============setup===========")
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.gmail.com/")

    yield page

    print("==============tear down==========")
    page.close()
    context.close()
    browser.close()


@pytest.mark.usefixtures("init")
def test_gmail_title():
    print("veriying gmail title method")


@pytest.mark.usefixtures("init")
def test_gmail_url():
    print("veriying gmail url method")
