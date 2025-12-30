from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.username_input = page.locator('#loginusername')
        self.password_input = page.locator('#loginpassword')
        self.login_button = page.get_by_role('button', name='Log in')
        self.close_button = page.get_by_role('button', name='Close')
        self.login_username_display = page.locator('#nameofuser')

    def login(self, username: str, password: str):
        self.username_input.clear()
        self.username_input.fill(username)
        self.password_input.clear()
        self.password_input.fill(password)
        self.login_button.click()
        self.page.wait_for_timeout(4000)  # Wait for login to process   

    def close_login_modal(self):
        self.close_button.click()

    def get_logged_in_username(self) -> str:
        self.page.wait_for_timeout(4000)
        return self.login_username_display.inner_text()
