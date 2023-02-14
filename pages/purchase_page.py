import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Purchase(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    choice_magazine_button = "//button[@type='submit']"
    list_button = "/html/body/mvid-root/mvid-modals-container/div[1]/mvid-modal/div/div/div/div/mvid-pickup-selector-modal/div/div[1]/div[3]/mvid-tabs/div/ul/li[2]/button"
    select_magazine = "/html/body/mvid-root/mvid-modals-container/div[1]/mvid-modal/div/div/div/div/mvid-pickup-selector-modal/div/div[2]/div[1]/mvid-pickup-list/div/table/div/tr[3]"
    button_zaberu = "/html/body/mvid-root/mvid-modals-container/div[1]/mvid-modal/div/div/div/div/mvid-pickup-selector-modal/div/div[2]/div[2]/mvid-pickup-info-store/div[2]/div/mvid-button/button"
    button_next = "/html/body/mvid-root/div/ng-component/ng-component/mvid-layout/div/main/div/div/div[2]/mvid-checkout-total/section/div[2]/div/mvid-payment-button/button"




    # Getters

    def get_choice_magazine_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.choice_magazine_button)))
    def get_list_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.list_button)))

    def get_select_magazine(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_magazine)))

    def get_button_zaberu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_zaberu)))

    def get_button_next(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_next)))

    # Actions

    def click_choice_magazine_button(self):
        self.get_choice_magazine_button().click()
        print("Click Choice magazine button")

    def click_list_button(self):
        self.get_list_button().click()
        print("Click list button")

    def click_select_magazine(self):
        self.get_select_magazine().click()
        print("Click select magazine")

    def click_button_zaberu(self):
        self.get_button_zaberu().click()
        print("Click button zaberu")

    def click_button_next(self):
        self.get_button_next().click()
        print("Click button next")

    # Methods
    def purchase_step_1(self):
        self.get_current_url()
        time.sleep(5)
        self.click_choice_magazine_button()
        time.sleep(3)
        self.click_list_button()
        self.click_select_magazine()
        self.assert_url("https://www.mvideo.ru/purchase/step1")
        time.sleep(3)
        self.click_button_zaberu()
        time.sleep(3)
        self.click_button_next()
        time.sleep(3)


