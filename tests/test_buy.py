import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from pages.cart_page import Cart_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.purchase_page import Purchase
from pages.select_page import Select_product


def test_buy_product_1(set_up,set_group):
    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(executable_path='C:\\Users\\elise\\PycharmProjects\\resource\\chromedriver.exe',
                              chrome_options=options)
    # webdriver.Firefox(executable_path='C:\\Users\\elise\\PycharmProjects\\resource\\geckodriver.exe')

    print("Start test 1")

    mp = Main_page(driver)
    mp.get_window()
    mp.click_all_smartphone()

    sp = Select_product(driver)
    sp.click_add_select_product()

    mp.click_select_cart()
    time.sleep(5)

    cp = Cart_page(driver)
    cp.product_confirmation()

    pp = Purchase(driver)
    pp.purchase_step_1()

    lp = Login_page(driver)
    lp.autorisation()

    print("Finish Test 1")
    time.sleep(10)


def test_buy_product_2(set_up):
    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(executable_path='C:\\Users\\elise\\PycharmProjects\\resource\\chromedriver.exe',
                              chrome_options=options)

    print("Start test 2")

    mp = Main_page(driver)
    mp.get_window()
    mp.click_all_computers()
    mp.click_select_cart()

    print("Finish Test 2")
    time.sleep(10)


def test_buy_product_3(set_up):
    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(executable_path='C:\\Users\\elise\\PycharmProjects\\resource\\chromedriver.exe',
                              chrome_options=options)

    print("Start test 3")

    mp = Main_page(driver)
    mp.get_window()
    mp.click_all_tv()
    mp.click_select_cart()

    print("Finish Test 3")
    time.sleep(10)
