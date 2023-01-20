from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #для явного ожидания
from base.base_class import Base


class Assorty_page(Base):


    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g


    # Locators - локаторы

    open_model = "//*[@id='item_container_2019072__ID']"

    # Locators assert - локаторы для проверки

    main_word = "//h1[@itemprop='name']"

    # Getters - условия

    def get_open_model(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.open_model)))

    def get_main_word(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    # Actions - действия

    def click_open_model(self):
        self.get_open_model().click()
        print("Клик открытия модели часов")


    # Methods - методы

    def select_open_model(self):
        self.get_current_url()                                                                  # Узнать нынешний url
        self.click_open_model()                                                                 # Открыть каталог
        self.assert_word(self.get_main_word(), "Смарт-часы Huawei Watch GT3 Active черные")     # Проверка по слову