import re
from playwright.sync_api import sync_playwright, expect
import pytest


def init(p: sync_playwright = None):
    print("Demo App Test Initialized")
    browser = p.chromium.launch(headless=False,slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    return browser, page

@pytest.mark.skip
def test_page_title():
    with sync_playwright() as p:
        browser, page = init(p)
        page.goto('https://globalsqa.com/angularJs-protractor/BankingProject/#/login')
        page.wait_for_load_state('networkidle')
        print(f'Page Title is: {page.title()}')
        browser.close()


@pytest.mark.parametrize("user",['Harry Potter','Hermoine Granger','Ron Weasly'])
def test_login_with_user(user: str):
    with sync_playwright() as p:
        browser, page = init(p)
        page.goto('https://globalsqa.com/angularJs-protractor/BankingProject/#/login')
        customers_btn = page.locator('button[ng-click="customer()"]')
        customers_btn.click()
        user_dropdown = page.locator('select#userSelect')
        user_dropdown.select_option(label=user)
        login_btn = page.get_by_role('button',name=re.compile('Login',re.IGNORECASE))
        expect(login_btn).to_be_visible(timeout=3000)
        login_btn.click()

        welcome_msg = page.locator('div > strong:nth-child(1)').nth(0).text_content()
        print(f'Login Welcome Message: {welcome_msg}')

        logout_btn = page.get_by_role('button', name='Logout')
        logout_btn.click()

        browser.close()
