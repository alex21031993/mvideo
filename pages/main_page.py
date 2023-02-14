import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from base.base_class import Base


class Main_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    catalog = "//button[@class='button button--with-icon ng-star-inserted']"
    telephone = "//mvid-catalog-last-level-category[@_ngcontent-serverapp-c172='']"
    computers = "//span[@_ngcontent-serverapp-c155='']"
    tv_video = "//span[@_ngcontent-serverapp-c155='']"
    # Select Cart
    select_cart = "//mvid-icon[@type = 'cart']"

    #Getters
    def get_catalog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog)))

    def get_telephone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.telephone)))

    def get_computers(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.computers)))

    def get_tv_video(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.tv_video)))

    def get_select_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_cart)))

    #Actions

    def click_catalog(self):
        self.get_catalog().click()
        print("Click catalog")

    def click_telephone(self):
        action = ActionChains(self.driver)
        action.move_by_offset(0, 200).perform()
        self.get_telephone().click()
        print("Click Telephone")

    def click_computers(self):
        action = ActionChains(self.driver)
        action.move_by_offset(0, 250).perform()
        self.get_computers().click()
        print("Click Computers")

    def click_tv_video(self):
        action = ActionChains(self.driver)
        action.move_by_offset(0, 300).perform()
        self.get_tv_video().click()
        print("Click TV video")

    def click_select_cart(self):
        self.get_select_cart().click()
        print("Click Select Cart")
        self.assert_url("https://www.mvideo.ru/cart")
        time.sleep(5)
        self.get_screenshot()


    #Methods
    def get_window(self):
        self.driver.get(self.url)
        self.driver.maximize_window()


    def click_all_smartphone(self):
        self.get_current_url()
        self.click_catalog()
        self.click_telephone()
        time.sleep(3)

    def click_all_computers(self):
        self.get_current_url()
        self.click_catalog()
        self.click_computers()
        time.sleep(3)

    def click_all_tv(self):
        self.get_current_url()
        self.click_catalog()
        self.click_tv_video()
        time.sleep(3)



