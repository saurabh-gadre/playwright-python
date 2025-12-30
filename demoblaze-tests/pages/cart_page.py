from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.place_order_btn = page.locator('button[data-target="#orderModal"]')
        self.total_price = page.locator('#totalp')
        self.cart_table_rows = page.locator('tr.success')
        self.product_delete_link = page.locator('tr.success td:nth-child(4) a')

    def get_total_price(self):
        return self.total_price.inner_text()

    def validate_total_price(self):
        sum = 0
        for price in self.cart_table_rows.locator('td:nth-child(3)').all():
            sum += int(price.inner_text())
        print(f'Actual Products Sum: ${sum}, Expected Products Sum: ${self.get_total_price()}')
        assert sum == int(self.get_total_price()), f"Expected Sum '{sum}', but got '{self.get_total_price()}'"

    def validate_first_added_product_in_cart(self, expected_name, expected_price):
        if self.cart_table_rows.count() > 1:
            actual_name = self.cart_table_rows.nth(1).locator('td:nth-child(2)').inner_text()
            actual_price = self.cart_table_rows.nth(1).locator('td:nth-child(3)').inner_text()
        else:
            actual_name = self.cart_table_rows.locator('td:nth-child(2)').inner_text()
            actual_price = self.cart_table_rows.locator('td:nth-child(3)').inner_text()
        assert actual_name == expected_name, f"Expected product name '{expected_name}', but got '{actual_name}'"
        assert actual_price == expected_price, f"Expected product price '{expected_price}', but got '{actual_price}'"

    def delete_first_product_from_cart(self):
        self.product_delete_link.click()
        self.page.wait_for_timeout(2000)  # Wait for the cart to update

    def place_order(self):
        self.place_order_btn.click()

    def delete_existing_products_in_cart(self):
        try:
            delete_btn_count = self.product_delete_link.count()
            for i in range(delete_btn_count):
                self.product_delete_link.nth(0).click()
                self.product_delete_link.nth(0).wait_for(state='detached')
        except TimeoutError as e:
            print('Delete Links are not present', e)
