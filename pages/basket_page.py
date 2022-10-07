from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):

    def is_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ELEMENTS), "Basket isn't empty!"

    def is_empty_basket_text_present(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), "Empty basket text is missing!"
