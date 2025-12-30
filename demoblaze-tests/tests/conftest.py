import os

import pytest
from playwright.sync_api import sync_playwright

# from utils import secrets_mgr


@pytest.fixture(scope='session')
def page():
    with sync_playwright() as playwright:
        # Headed Mode
        # browser = playwright.chromium.launch(headless=False, args=['--start-maximized'])
        # Headless Mode
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context(no_viewport=True)
        page = context.new_page()
        yield page
        context.close()
        browser.close()


@pytest.fixture(scope='session')
def setup(page):
    page.set_default_timeout(6000)
    yield page
    page.close()


@pytest.fixture(scope='session')
def get_user_credentials():
    return {
        "username": "admin",
        "password": os.environ["PASSWORD"]
    }
