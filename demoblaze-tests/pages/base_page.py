from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self, url: str):
        self.page.goto(url)
        self.page.wait_for_load_state('load')

    def click(self, selector: str):
        self.page.click(selector=selector)

    def fill(self, selector: str, text: str):
        self.page.locator(selector=selector).fill(text)

    def get_text(self, selector: str) -> str:
        return self.page.locator(selector=selector).inner_text()
