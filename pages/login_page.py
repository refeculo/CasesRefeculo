from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #для явного ожидания
from base.base_class import Base

class Login_page(Base):



    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g


    # Locators - локаторы

    user_name = "//input[@id='user-name']"
    password = "//input[@id='password']"
    login_button = "//input[@id='login-button']"

    # Locators assert - локаторы для проверки

    main_word = "//span[@class='title']"


    # Getters - условия

    def get_user_name(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))


    # Actions - действия

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Ввод логина")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Ввод пароля")

    def click_login_button(self):
        self.get_login_button().click()
        print("Клик на кнопку авторизации")


    # Methods - методы

    def authorization(self):
        self.driver_g.get(self.url)                        # Открытие браузера
        self.driver_g.maximize_window()                    # Расширить браузер
        self.get_current_url()                             # Узнать нынешний url
        self.input_user_name("standard_user")              # Ввести логин
        self.input_password("secret_sauce")                # Ввести пароль
        self.click_login_button()                          # Нажать на кнопку авторизации
        self.assert_word(self.get_main_word(), "PRODUCTS") # Проверка по слову