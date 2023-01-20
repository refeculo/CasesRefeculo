from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #для явного ожидания
from base.base_class import Base


class Model_page(Base):


    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g


    # Locators - локаторы

    check_foto_2 = "//a[@title='Смарт-часы Huawei Watch GT3 Active черные Изображение 2']"
    check_foto_3 = "//a[@title='Смарт-часы Huawei Watch GT3 Active черные Изображение 3']"
    check_foto_4 = "//a[@title='Смарт-часы Huawei Watch GT3 Active черные Изображение 4']"
    check_foto_5 = "//a[@title='Смарт-часы Huawei Watch GT3 Active черные Изображение 5']"
    buy_button = "//*[@id='goods_content']/div[1]/div[4]/div[2]/div[1]/div[3]/span/a"
    checkout = "//*[@id='js__popup_addedToCart__cartLinkID']"


    # Getters - условия

    def get_check_foto_2(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.check_foto_2)))

    def get_check_foto_3(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.check_foto_3)))

    def get_check_foto_4(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.check_foto_4)))

    def get_check_foto_5(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.check_foto_5)))

    def get_buy_button(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.buy_button)))

    def get_checkout(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout)))


    # Actions - действия

    def click_check_foto_2(self):
        self.get_check_foto_2().click()
        print("Посмотреть 2 фотографию")

    def click_check_foto_3(self):
        self.get_check_foto_3().click()
        print("Посмотреть 3 фотографию")

    def click_check_foto_4(self):
        self.get_check_foto_4().click()
        print("Посмотреть 4 фотографию")

    def click_check_foto_5(self):
        self.get_check_foto_5().click()
        print("Посмотреть 5 фотографию")

    def click_buy_button(self):
        self.get_buy_button().click()
        print("Клик по кнопке купить")

    def click_checkout(self):
        self.get_checkout().click()
        print("Клик по кнопки оформить")


    # Methods - методы

    def buy_model(self):
        self.get_current_url()            # Узнать нынешний url
        self.get_screenshot()             # Получить скриншот
        self.click_check_foto_2()         # Посмотреть 2 фотографию
        self.click_check_foto_3()         # Посмотреть 3 фотографию
        self.click_check_foto_4()         # Посмотреть 4 фотографию
        self.click_check_foto_5()         # Посмотреть 5 фотографию
        self.click_buy_button()           # Клик по кнопке купить
        self.click_checkout()             # Клик по кнопки оформить


