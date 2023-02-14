import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Login_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    full_name = "//input[@formcontrolname = 'fullName']"
    mobile_number = "//input[@formcontrolname = 'phone']"
    email = "//input[@formcontrolname = 'email']"
    main_word = "/html/body/mvid-root/div/ng-component/ng-component/mvid-layout/div/main/div/h1"
    button_payment = "/html/body/mvid-root/div/ng-component/ng-component/mvid-layout/div/main/div/div/div[2]/div/div/mvid-checkout-total/section/div[2]/div[1]/mvid-payment-button/button"
    button_bank_cart = "/html/body/mvid-root/div/ng-component/ng-component/mvid-layout/div/main/div/div/div[1]/div[2]/mvid-checkout-payment/div/ul/li[2]/mvid-checkout-option/div"

    # Getters

    def get_full_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.full_name)))

    def get_mobile_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mobile_number)))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_button_payment(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_payment)))

    def get_button_bank_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_bank_cart)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))


    # Actions

    def input_full_name(self, full_name):
        self.get_full_name().send_keys(full_name)
        print("input full name")

    def input_mobile_number(self, mobile_number):
        self.get_mobile_number().send_keys(mobile_number)
        print("input mobile number")

    def input_email(self, email):
        self.get_email().send_keys(email)
        print("input email")

    def click_button_payment(self):
        self.get_button_payment().click()
        print("Click button payment")

    def click_button_bank_cart(self):
        self.get_button_bank_cart().click()
        print("Click button bank cart")

    # Methods
    def autorisation(self):
        self.get_current_url()
        self.assert_word(self.get_main_word(), "Оформление заказа. Шаг 2 из 2")
        self.click_button_bank_cart()
        self.driver.execute_script("window.scrollTo(0,400)")
        time.sleep(3)
        self.input_full_name("Иван Иванов")
        self.input_mobile_number("9325512325")
        self.input_email("ivanivanov@mail.ru")
        time.sleep(3)
        self.click_button_payment()
        time.sleep(3)



