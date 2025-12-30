import re
from playwright.sync_api import Playwright, sync_playwright, Page, expect
import pytest


def init(p: sync_playwright = None):
    print("Demo App Test Initialized")
    browser = p.chromium.launch(headless=False,slow_mo=500, args=['--start-maximized'])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    return browser, page


def test_web_form():
    with sync_playwright() as p:
        browser, page = init(p)
        page.goto('https://formy-project.herokuapp.com/form')
        page.get_by_label('First name').fill('John')
        page.get_by_placeholder('Enter last name').fill('Doe')
        page.locator('input:below(input[placeholder="Enter your job title"])').nth(0).click()
        page.locator('input[value="checkbox-2"]:near(input[id="checkbox-1"])').click() #near, below, above, left-of, right-of

        select_element = page.locator('#select-menu')
        select_element.hover()
        select_element.select_option(label='5-9')
        select_element.select_option(value='4')

        calendar_input = page.locator('#datepicker')
        calendar_input.click()
        page.locator('//table[@class="table-condensed"]/tbody/tr/td[@class="today day"]').click()
        page.get_by_role('button', name='Submit').click()

        page.wait_for_selector('[role="alert"]')
        message = page.locator('[role="alert"]')
        expect(page.locator('text=Thanks for submitting your form')).to_be_visible()
        print("Form submitted successfully with message:", message.text_content())
        expect(message).to_contain_text('The form was successfully submitted!')
        browser.close()