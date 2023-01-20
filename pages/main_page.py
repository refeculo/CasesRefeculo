from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #для явного ожидания
from base.base_class import Base


class Main_page(Base):

    url = "https://www.onlinetrade.ru/"

    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g


    # Locators - локаторы

    open_catalog = "//*[@id='main_area']/div[2]/div/div/div[2]/a[1]"
    open_smart_chasy = "//*[@id='ssCM_2325_ID']/li[3]/a"

    # Locators assert - локаторы для проверки

    main_word = "//*[@id='main_area']/div[4]/div/h1"


    # Getters - условия

    def get_open_catalog(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.open_catalog)))

    def get_open_smart_chasy(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.open_smart_chasy)))

    def get_main_word(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))


    # Actions - действия

    def click_open_catalog(self):
        self.get_open_catalog().click()
        print("Клик открытия каталога")

    def click_open_smart_chasy(self):
        self.get_open_smart_chasy().click()
        print("Войти в категорию смарт-часов")


    # Methods - методы

    def select_menu(self):
        self.driver_g.get(self.url)                                 # Открытие браузера
        self.driver_g.maximize_window()                             # Расширить браузер
        self.get_current_url()                                      # Узнать нынешний url
        self.click_open_catalog()                                   # Открыть каталог
        self.click_open_smart_chasy()                               # Вход в категорию смарт часов
        self.assert_word(self.get_main_word(), "Смарт-часы")        # Проверка по слову

