from pages.base_page import BasePage
from pages.locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException

import math


class ProductPage(BasePage):

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def add_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        button.click()

    def main_checks(self):

        self.is_element_added_to_cart()
        self.is_valid_price()

    def is_element_added_to_cart(self):
        alert_name = self.browser.find_element(*ProductPageLocators.ALERT_BOOK_NAME).text
        name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        assert alert_name == name, "Book isn't added!"

    def is_valid_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        alert_price = self.browser.find_element(*ProductPageLocators.ALERT_PRICE).text
        assert price == alert_price, "Price doesn't match!"
