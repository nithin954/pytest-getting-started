from playwright.sync_api import Page, expect

"""
regular cmd:-  pytest pytest_test/test_demo_03_parallel.py -vs --headed
parallel cmd:- pytest pytest_test/test_demo_03_parallel.py -vs --headed -n 4
"""


def test_google(page: Page):
    page.goto("https://www.google.com/")
    expect(page).to_have_title("Google")


def test_gmail(page: Page):
    page.goto("https://www.gmail.com/")
    expect(page).to_have_title("Gmail")


def test_insta(page: Page):
    page.goto("https://www.instagram.com/")
    expect(page).to_have_title("Instagram")


def test_playwright(page: Page):
    page.goto("https://playwright.dev/python/")
    expect(page).to_have_title(
        "Fast and reliable end-to-end testing for modern web apps | Playwright Python"
    )
