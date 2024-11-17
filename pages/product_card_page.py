from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from base.base_class import Base


class Product_card_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    close_button = "//div[@class='d-modal__close-button']"
    size_button = "//div[@class='_sizeValue_8karg_281' and contains(text(), '46 RUS')]"
    basket_button = "//div[@class='recaptcha _recaptcha_vuhwd_7']"
    basket = "//a[@class='_root_c16u7_2 _root_aroml_2 _secondaryLabel_aroml_13']"

    # Getters

    def get_close_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.close_button)))

    def get_size_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.size_button)))

    def get_basket_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.basket_button)))

    def get_close_button_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.close_button)))

    def get_basket(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.basket)))




    # Actions
    def click_close_button(self):
        self.get_close_button().click()
        print("Click close button")

    def click_size_button(self):
        self.get_size_button().click()
        print("Click size button")

    def click_basket_button(self):
        self.get_basket_button().click()
        print("Click basket button")

    def click_close_button_2(self):
        self.get_close_button_2().click()
        print("Click close button 2")

    def click_basket(self):
        self.get_basket().click()
        print("Click basket")


    # Methods
    def product_basket(self):
        self.get_current_url()
        self.click_close_button()
        self.click_size_button()
        self.click_basket_button()
        self.get_close_button_2()
        self.click_basket()

