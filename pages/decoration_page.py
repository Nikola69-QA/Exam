from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from base.base_class import Base


class Decoration_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    select_point = "//button[@class='x-button x-button_secondaryFilledWeb7184 x-button_48 _button_wtyxg_2 ui-checkout-form__button-pickup-select']"
    picup_point = "(//div[@class='_content_1oris_12'])[1]"
    button_select_point = "//button[@class='x-button x-button_primaryPremium x-button_48 _button_nrs52_55 ui-select-pickups__button-submit']"
    first_name = "(//div[@class='input-material__placeholder input-material__placeholder_checkout'])[2]"
    last_name = "(//div[@class='input-material__placeholder input-material__placeholder_checkout'])[3]"
    phone = "(//div[@class='input-material__placeholder input-material__placeholder_checkout'])[4]"
    email = "(//div[@class='input-material__placeholder input-material__placeholder_checkout'])[5]"



    # Getters

    def get_select_point(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_point)))

    def get_picup_point(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.picup_point)))

    def get_button_select_point(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_select_point)))

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone)))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))


    # Actions
    def click_select_point(self):
        self.get_select_point().click()
        print("Click select point")

    def click_picup_point(self):
        self.get_select_point().click()
        print("Click picup_point")

    def click_button_select_point(self):
        self.get_button_select_point().click()
        print("Click button select point")

    def input_get_first_name(self,first_name ):
        self.get_first_name().send_keys(first_name)
        print("Input first name")

    def input_get_last_name(self,last_name):
        self.get_last_name().send_keys(last_name)
        print("Input last name")

    def input_get_phone(self,phone):
        self.get_phone().send_keys(phone)
        print("Input phone")

    def input_get_email(self,email):
        self.get_email().send_keys(email)
        print("Input email")


    # Methods
    def decoration_select(self):
        self.get_current_url()
        self.click_select_point()
        self.click_picup_point()
        self.click_button_select_point()
        self.input_get_first_name("Ivan")
        self.input_get_last_name("Ivanov")
        self.input_get_phone("9999999999")
        self.input_get_email("test@test.ru")


