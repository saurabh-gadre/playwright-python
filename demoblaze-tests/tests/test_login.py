import os

import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage
# from utils import secrets_mgr


def handle_dialog(dialog):
    global alert_message
    alert_message = dialog.message
    dialog.accept()
    return dialog.message


@pytest.mark.smoke
@pytest.mark.parametrize('username,password', [('adminuzer', 'admin123'), ('demouser', 'admin123')])
def test_login_with_invalid_credentials(setup, username, password):
    page = setup
    home_page = HomePage(page)
    login_page = LoginPage(page)

    home_page.goto("https://www.demoblaze.com/")
    home_page.go_to_login_page()

    page.on('dialog', handle_dialog)
    login_page.login(username, password)
    print(f'\nAlert Text: {alert_message}')
    assert alert_message in ['User does not exist.', 'Wrong password.']


@pytest.mark.smoke
@pytest.mark.parametrize('username,password', [
    pytest.param('adminuzer', 'admin123', marks=pytest.mark.xfail),
    pytest.param('demouser', 'admin123', marks=pytest.mark.xfail), ('admin', os.environ["PASSWORD"])])
def test_login_with_different_credentials(setup, username, password):
    page = setup
    home_page = HomePage(page)
    login_page = LoginPage(page)

    home_page.goto("https://www.demoblaze.com/")
    home_page.go_to_login_page()
    login_page.login(username, password)
    logged_in_username = login_page.get_logged_in_username()
    assert logged_in_username == f"Welcome {username}", "Incorrect username displayed."


@pytest.mark.smoke
def test_login_with_valid_credentials(setup, get_user_credentials):
    page = setup
    home_page = HomePage(page)
    login_page = LoginPage(page)

    home_page.goto("https://www.demoblaze.com/")
    home_page.go_to_login_page()
    credentials = get_user_credentials
    user_name = credentials["username"]
    password = credentials["password"]

    login_page.login(user_name, password)
    logged_in_username = login_page.get_logged_in_username()
    assert logged_in_username == f"Welcome {user_name}", "Incorrect username displayed."


@pytest.mark.smoke
def test_login_logout(setup, get_user_credentials):
    page = setup
    home_page = HomePage(page)
    test_login_with_valid_credentials(page, get_user_credentials)

    home_page.logout()
    assert not home_page.logout_page.is_visible()
