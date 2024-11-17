from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from base.base_class import Base


class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    decoration_button = "//button[@class='x-button x-button_primaryPremium x-button_52 _button_c8qt8_6']"

    # Getters

    def get_decoration_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.decoration_button)))



    # Actions
    def click_decoration_button(self):
        self.get_decoration_button().click()
        print("Click decoration button")


    # Methods
    def product_confirmation(self):
        self.get_current_url()
        self.click_decoration_button()
