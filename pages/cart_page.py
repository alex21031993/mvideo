import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Cart_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    checkout_button = "//button[@size='large']"
    skip_button = "//button[@color='secondary']"

    # Getters

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))
    def get_skip_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.skip_button)))



    # Actions

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("Click Checkout button")

    def click_skip_button(self):
        self.get_skip_button().click()
        print("Click Skip button")

    # Methods
    def product_confirmation(self):
        self.get_current_url()
        self.click_checkout_button()
        time.sleep(3)
        self.click_skip_button()

