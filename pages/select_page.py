import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from base.base_class import Base



class Select_product(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators Categories
    smartfony = "/html/body/mvid-root/div/mvid-primary-layout/mvid-layout/div/main/mvid-plp/mvid-product-list-block/mvid-filters-list/div/div[1]/div/div/mvid-accordion[1]/div/div/div/mvid-filter-checkbox-list/form/div/div[1]/mvid-checkbox/div/span/a"
    iphone = "/html/body/mvid-root/div/mvid-primary-layout/mvid-layout/div/main/mvid-plp/mvid-product-list-block/mvid-filters-list/div/div[1]/div/div/mvid-accordion[1]/div/div/div/mvid-filter-checkbox-list/form/div/div[2]/mvid-checkbox/div/span/a"

    # Brends
    xiaomi = "/html/body/mvid-root/div/mvid-primary-layout/mvid-layout/div/main/mvid-plp/mvid-product-list-block/mvid-filters-list/div/div[1]/div/div/mvid-accordion[2]/div/div/div/mvid-filter-checkbox-list/form/div/div/mvid-checkbox/div/span"
    apple = "/html/body/mvid-root/div/mvid-primary-layout/mvid-layout/div/main/mvid-plp/mvid-product-list-block/mvid-filters-list/div/div[1]/div/div/mvid-accordion[2]/div/div/div/mvid-filter-checkbox-list/form/div/div[1]/mvid-checkbox/div/span/a"
    show_more = "/html/body/mvid-root/div/mvid-primary-layout/mvid-layout/div/main/mvid-plp/mvid-product-list-block/mvid-filters-list/div/div[1]/div/div/mvid-accordion[2]/div/div/div/mvid-filter-checkbox-list/form/p"

    # Button_price
    button_price_left = "/html/body/mvid-root/div/mvid-primary-layout/mvid-layout/div/main/mvid-plp/mvid-product-list-block/mvid-filters-list/div/div[1]/div/div/mvid-accordion[3]/div/div/div/mvid-price-facet/div/div/mvid-slider/div/div/button[1]"
    button_price_right = "/html/body/mvid-root/div/mvid-primary-layout/mvid-layout/div/main/mvid-plp/mvid-product-list-block/mvid-filters-list/div/div[1]/div/div/mvid-accordion[3]/div/div/div/mvid-price-facet/div/div/mvid-slider/div/div/button[2]"

    # Products
    add_cart_product_1 = "/html/body/mvid-root/div/mvid-primary-layout/mvid-layout/div/main/mvid-plp/mvid-product-list-block/div[2]/mvid-product-list/mvid-plp-product-cards-layout/div/div[1]/mvid-plp-product-card/div/div[3]/mvid-plp-product-checkout/div/mvid-preorder-v2-wrapper/div/mvid-plp-checkout-tooltip/mvid-plp-cart-button/mvid-button/button"
    add_cart_product_2 = "/html/body/mvid-root/div/mvid-primary-layout/mvid-layout/div/main/mvid-plp/mvid-product-list-block/div[2]/mvid-product-list/mvid-plp-product-cards-layout/div/div[2]/mvid-plp-product-card/div/div[3]/mvid-plp-product-checkout/div/mvid-preorder-v2-wrapper/div/mvid-plp-checkout-tooltip/mvid-plp-cart-button/mvid-button/button"

    # Input
    poisk_znacheniy = "//input[@id = '4']"



    # Price
    name_product_1 = "/html/body/mvid-root/div/mvid-primary-layout/mvid-layout/div/div[1]/mvid-header-container/mvid-header/header/div[2]/div/mvid-tap-bar/div/div[6]/mvid-header-icon/div/mvid-header-icon-tooltip/div/div[1]/div[2]/div/div/div/div[1]/div/a"
    name_product_2 = "/html/body/mvid-root/div/mvid-primary-layout/mvid-layout/div/div[1]/mvid-header-container/mvid-header/header/div[2]/div/mvid-tap-bar/div/div[6]/mvid-header-icon/div/mvid-header-icon-tooltip/div/div[1]/div[1]/div/div/div/div[1]/div/a"
    # Getters
    def get_smartfony(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.smartfony)))

    def get_iphone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.iphone)))

    def get_show_more(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.show_more)))

    def get_xiaomi(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.xiaomi)))

    def get_apple(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.apple)))

    def get_button_left(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_price_left)))

    def get_button_right(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_price_right)))

    def get_poisk(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.poisk_znacheniy)))


    def get_add_cart_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_cart_product_1)))


    def get_add_cart_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_cart_product_2)))

    def get_name_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_product_1)))

    def get_name_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_product_2)))



    # Actions

    def click_smartfony(self):
        self.get_smartfony().click()
        print("Click smartfony")

    def click_iphone(self):
        self.get_iphone().click()
        print("Click iphone")

    def click_show_more(self):
        self.driver.execute_script("window.scrollTo(0,400)")
        self.get_show_more().click()
        time.sleep(2)
        print("Click show more")

    def click_show_xiaomi(self):
        self.get_xiaomi().click()
        print("Click show Xiaomi")

    def click_show_apple(self):
        self.get_apple().click()
        print("Click show apple")

    def click_button_left(self, x, y):
        action = ActionChains(self.driver)
        square = self.driver.find_element(By.XPATH, self.button_price_left)
        action.click_and_hold(square).move_by_offset(x, y).release().perform()
        print("Click Button left")

    def click_button_right(self, x, y):
        action = ActionChains(self.driver)
        square = self.driver.find_element(By.XPATH, self.button_price_right)  # id Xpath
        action.click_and_hold(square).move_by_offset(x, y).release().perform()
        # print("Square +")
        self.get_button_left().click()
        print("Click Button right")

    def input_poisk_znacheniy(self, poisk):
        self.get_poisk().send_keys(poisk)
        print("Input poisk znacheniy")

    def click_add_cart_product_1(self):
        time.sleep(5)
        self.get_add_cart_product_1().click()
        print("Add to cart product 1")


    def click_add_cart_product_2(self):
        time.sleep(5)
        self.get_add_cart_product_2().click()
        print("Add to cart product 2")




    # Methods

    def click_add_select_product(self):
        self.click_smartfony()
        self.click_show_more()
        self.input_poisk_znacheniy("Xiaomi")
        time.sleep(3)
        self.click_show_xiaomi()
        time.sleep(2)
        self.click_button_left(200, 0)
        print("Good Price Left")
        self.click_add_cart_product_1()
        self.assert_word(self.get_name_product_1(), "Смартфон Xiaomi 12T 256Gb Black")
        time.sleep(2)
        self.click_add_cart_product_2()
        time.sleep(2)
        self.assert_word(self.get_name_product_2(), "Смартфон Xiaomi 11T 8GB+256GB Gray")
