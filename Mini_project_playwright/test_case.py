from playwright.sync_api import sync_playwright
from POM.login import Login

def test_login_scenario():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://v2.zenclass.in/login")
        login = Login(page)
        login.login()
        page.close()
        browser.close()
