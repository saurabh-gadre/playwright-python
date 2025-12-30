from pages.base_page import BasePage


class ProductPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.add_to_cart_button = page.locator('a.btn-success')
        self.product_name = page.locator('h2.name')
        self.product_price = page.locator('h3.price-container')

    def add_product_to_cart(self):
        self.add_to_cart_button.click()
        self.page.wait_for_timeout(2000)  # Wait for potential alert to appear

    def get_product_name(self):
        return self.product_name.inner_text()

    def get_product_price(self):
        return self.product_price.inner_text()

    def validate_product_details(self, expected_name, expected_price):
        actual_name = self.get_product_name()
        # Assuming price format is like "$790 *includes tax"
        actual_price = self.get_product_price().split(" ")[0].split("$")[1]
        print(f"Actual Name: {actual_name}, Actual Price: ${actual_price}")
        assert actual_name == expected_name, f"Expected product name '{expected_name}', but got '{actual_name}'"
        assert actual_price == expected_price, f"Expected product price '{expected_price}', but got '{actual_price}'"

    def handle_alert(self):
        self.page.on('dialog', lambda dialog: dialog.accept())
        self.page.wait_for_timeout(2000)  # Wait for alert handling to complete
