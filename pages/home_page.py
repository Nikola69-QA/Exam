from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from base.base_class import Base


class Home_page(Base):
    """Сайт на который необходимо перейти"""
    url = 'https://www.lamoda.ru/men-home/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators перехода в подраздел одежда
    select_chapter = "//a[@href='/c/477/clothes-muzhskaya-odezhda/?sitelink=topmenuM&l=3']"

    # Getters
    def get_select_chapter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_chapter)))




    # Actions кликаем на подраздел одежда

    def click_select_chapter(self):
        self.get_select_chapter().click()
        print("Click select chapter clothes")

    # Methods вызываем методы для перехода
    def clolthes_men(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_select_chapter()
