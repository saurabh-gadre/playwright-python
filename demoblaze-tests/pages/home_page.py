from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.login_page = page.locator('#login2')
        self.signup_page = page.locator('#signin2')
        self.contact_page = page.locator('[data-target="#exampleModal"]')
        self.cart_page = page.locator('#cartur')
        self.home_page = page.locator('a:has-text("Home ")')
        self.categories = page.locator('.list-group a[id="itemc"]')
        self.phones_category = self.categories.nth(0)
        self.laptops_category = self.categories.nth(1)
        self.monitors_category = self.categories.nth(2)
        self.products_css_selector_str = 'h4[class="card-title"] a:has-text("{product_name}")'
        self.logout_page = page.locator('#logout2')
        self.page = page

    def go_to_login_page(self):
        self.login_page.click()

    def logout(self):
        self.logout_page.click()

    def go_to_signup_page(self):
        self.signup_page.click()

    def go_to_contact_page(self):
        self.contact_page.click()

    def go_to_cart_page(self):
        self.cart_page.click()
        self.page.wait_for_timeout(3000)

    def refresh_home_page(self):
        self.home_page.click()

    def select_category(self, category_name: str):
        category_map = {
            'Phones': self.phones_category,
            'Laptops': self.laptops_category,
            'Monitors': self.monitors_category
        }
        if category_name in category_map:
            category_map[category_name].click()
        else:
            raise ValueError(f"Category '{category_name}' not found.")

    def select_product(self, product_name: str):
        constructed_product_selector = self.products_css_selector_str.format(product_name=product_name)
        self.page.locator(constructed_product_selector).click()
        self.page.wait_for_timeout(2000)
