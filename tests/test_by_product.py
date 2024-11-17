import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager



from pages.cart_page import Cart_page
from pages.home_page import Home_page
from pages.clothes_page import Clothes_page
from pages.decoration_page import Decoration_page
from pages.product_card_page import Product_card_page


def test_buy_product():

    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))


    print("start test")

    clothes = Home_page(driver)
    clothes.clolthes_men()

    mp = Clothes_page(driver)
    mp.select_products()

    p = Product_card_page(driver)
    p.product_basket()

    cp = Cart_page(driver)
    cp.product_confirmation()

    d = Decoration_page(driver)
    d.decoration_select()


    print("Test finish")
    # time.sleep(10)
    driver.quit()


# cd C:\Users\Николай\PycharmProjects\finalAT\tests (для перехода в директорию с тестом)
# python -m pytest -s -v -k test_buy_product_3
# python -m pytest -s -v  test_by_product.py