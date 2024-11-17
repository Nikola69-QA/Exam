from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from base.base_class import Base


class Clothes_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators для выбора подраздела брюки джогеры
    select_joggers = "(//a[@href='/c/7602/clothes-men-joggers/'])[1]"
    clothes_trousers = "(//a[@href='/c/517/clothes-muzhskie-bryuki/'])[1]"
    materials = "(//span[@class='_title_pjvgk_43'])[2]"
    select_cotton = "//span[@class='_valueTitle_htwrd_47 _firstLetterUppercase_htwrd_52' and contains(text(), 'Хлопок')]"
    button_prim = "(//button[@type='button'])[3]"
    prices = "//span[@class='_title_pjvgk_43' and contains(text(), 'Цена')]"
    price_minimum = "//input[@name='minRange']"
    price_maximum = "//input[@name='maxRange']"

    select_prod = "(//div[@class='_area_552z7_8'])[1]"



    # Getters

    def get_clothes_trousers(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.clothes_trousers)))

    def get_select_joggers(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_joggers)))

    def get_materials(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.materials)))

    def get_select_cotton(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_cotton)))

    def get_button_prim(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_prim)))

    def get_prices(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.prices)))

    def get_price_minimum(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_minimum)))

    def get_price_maximum(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_maximum)))

    def get_select_prod(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_prod)))


    # Actions
    def click_clothes_trousers(self):
        self.get_clothes_trousers().click()
        print("Click clothes trousers")

    def click_select_joggers(self):
        self.get_select_joggers().click()
        print("Click select joggers")

    def click_materials(self):
        self.get_materials().click()
        print("Click materials")

    def click_select_cotton(self):
        self.get_select_cotton().click()
        print("Click select cotton")

    def click_button_prim(self):
        self.get_button_prim().click()
        print("Click button prim")

    def click_prices(self):
        self.get_prices().click()
        print("Click prices")

    def click_get_price_minimum(self,price_minimum):
        self.get_price_minimum().send_keys(price_minimum)
        print("Click price minimum")

    def click_get_price_maximum(self,price_maximum):
        self.get_price_minimum().send_keys(price_maximum)
        print("Click price maximum")

    def click_get_select_prod(self):
        self.get_price_minimum().click()
        print("Click select prod")


    # Methods
    def select_products(self):
        self.get_current_url()
        self.click_clothes_trousers()
        self.click_select_joggers()
        self.get_materials()
        self.get_select_cotton()
        self.click_button_prim()
        self.click_prices()
        self.click_get_price_minimum("1000")
        self.click_get_price_maximum("2000")
        self.click_get_select_prod()
        self.assert_url('https://www.lamoda.ru/men-home/')

