import pytest

from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.product_page import ProductPage


@pytest.fixture(scope="function")
def get_test_data():
    return {
        "product_category": "Laptops",
        "product_name": "Sony vaio i5",
        "product_price": "790"
    }


def initialize_pages(setup):
    page = setup
    home_page = HomePage(page)
    login_page = LoginPage(page)
    product_page = ProductPage(page)
    cart_page = CartPage(page)
    return home_page, login_page, product_page, cart_page


def test_add_product_to_cart(setup, get_user_credentials, get_test_data):
    home_page, login_page, product_page, cart_page = initialize_pages(setup)

    # Navigate to home page
    home_page.goto("https://www.demoblaze.com")
    # Go to login page and perform login
    home_page.go_to_login_page()
    login_page.login(get_user_credentials["username"], get_user_credentials["password"])

    # delete existing products in cart
    home_page.go_to_cart_page()
    cart_page.delete_existing_products_in_cart()

    # Select a product category and product
    home_page.refresh_home_page()
    home_page.select_category(get_test_data["product_category"])
    home_page.select_product(get_test_data["product_name"])

    # Add the product to the cart
    product_page.validate_product_details(get_test_data["product_name"], get_test_data["product_price"])
    product_page.handle_alert()
    product_page.add_product_to_cart()

    home_page.go_to_cart_page()
    # Validate the product in the cart
    cart_page.validate_first_added_product_in_cart(get_test_data["product_name"], get_test_data["product_price"])
    cart_page.validate_total_price()


def test_delete_product_to_cart(setup, get_user_credentials):
    home_page, login_page, product_page, cart_page = initialize_pages(setup)

    # Navigate to home page
    home_page.goto("https://www.demoblaze.com")
    # Go to login page and perform login
    home_page.go_to_login_page()
    login_page.login(get_user_credentials["username"], get_user_credentials["password"])

    # delete existing products in cart
    home_page.go_to_cart_page()
    cart_page.delete_existing_products_in_cart()
