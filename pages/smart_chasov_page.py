from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # для явного ожидания
from base.base_class import Base
from selenium.webdriver import ActionChains


class Smart_chasov_page(Base):

    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    # Locators - локаторы

    filter_in_stock = "//*[@id='l5950a4a1de00bc24202c5f78a0a726be']"
    filter_model_huawei = "//*[@id='lcd497331707025c970c57e8c81d39ea3']"
    open_filter_price = "//div[@title='Подобрать по цене в категории «Смарт-часы»']"
    clear_price_min = "//*[@id='price1']"
    filter_price_min = "//*[@id='price1']"
    clear_price_max = "//*[@id='price2']"
    filter_price_max = "//*[@id='price2']"
    scroll_color = "//div[@id='columnBlock__21746filter__ID']"
    open_filter_color = "//div[@title='Цвет в категории «Смарт-часы»']"
    filter_color_black = "//*[@id='lf7db97e847b201c1a4f0627f817f3b72']"
    pick_up_button = "//a[@title='Подобрать']"

    # Getters - условия

    def get_filter_in_stock(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_in_stock)))

    def get_filter_model_huawei(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_model_huawei)))

    def get_open_filter_price(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.open_filter_price)))

    def get_clear_price_min(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.clear_price_min)))

    def get_filter_price_min(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_price_min)))

    def get_clear_price_max(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.clear_price_max)))

    def get_filter_price_max(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_price_max)))

    def get_scroll_color(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.scroll_color)))

    def get_open_filter_color(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.open_filter_color)))

    def get_filter_color_black(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_color_black)))

    def get_pick_up_button(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.pick_up_button)))

    # Actions - действия

    def click_filter_in_stock(self):
        self.get_filter_in_stock().click()
        print("Клик фильтра в наличии")

    def click_filter_model_huawei(self):
        self.get_filter_model_huawei().click()
        print("Клик фильтра модели HUAWEI")

    def click_open_filter_price(self):
        self.get_open_filter_price().click()
        print("Клик открытия фильтра цена")

    def input_clear_price_min(self):
        self.get_filter_price_min().clear()
        print("Очистить поле минимальной цены")

    def input_filter_price_min(self, filter_price_min):
        self.get_filter_price_min().send_keys(filter_price_min)
        print("Ввод минимальной цены")

    def input_clear_price_max(self):
        self.get_filter_price_max().clear()
        print("Очистить поле максимальной цены")

    def input_filter_price_max(self, filter_price_max):
        self.get_filter_price_max().send_keys(filter_price_max)
        print("Ввод максимальной цены")

    def action_scroll_color(self):
        action = ActionChains(self.driver_g)
        action.move_to_element(self.get_scroll_color()).perform()
        print("Доскролить страницу до фильтра цвета")

    def click_open_filter_color(self):
        self.get_open_filter_color().click()
        print("Клик открытия фильтра цвета")

    def click_filter_color_black(self):
        self.get_filter_color_black().click()
        print("Клик фильтра цвета")

    def click_pick_up_button(self):
        self.get_pick_up_button().click()
        print("Клик кнопки подобрать")

    # Methods - методы

    def pick_up_model_smart_chasov(self):
        self.get_current_url()                      # Узнать нынешний url
        self.click_filter_in_stock()                # Кликнуть по фильтру 'в наличии'
        self.click_filter_model_huawei()            # Кликнуть по фильтру 'HUAWEI'
        self.click_open_filter_price()              # Открыть фильтр цены
        self.input_clear_price_min()                # Очистить минимальный фильтр цены
        self.input_filter_price_min("10000")        # Ввести минимальный фильтр цены
        self.input_clear_price_max()                # Очистить максимальный фильтр цены
        self.input_filter_price_max("20000")        # Ввести максимальный фильтр цены
        self.action_scroll_color()                  # Доскролить до фильтра цвета
        self.click_open_filter_color()              # Открыть фильтр цвета
        self.click_filter_color_black()             # Кликнуть по фильтру 'черный'
        self.click_pick_up_button()                 # Кликнуть по кнопку предложеные