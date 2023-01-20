import datetime

class Base():

    def __init__(self, driver_g):
        self.driver_g = driver_g


    # Метод получения url

    def get_current_url(self):
        get_url = self.driver_g.current_url
        print("\nНынешний url " + get_url)

    # Метод проверки по слову

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Проверка по слову "+ result + " прошла успешно")

    # Метод скриншота

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%d-%m-%Y %H-%M-%S")
        name_screenshot = "Скриншот " + now_date + ".png"
        print(name_screenshot)
        self.driver_g.save_screenshot("C:\\Users\\Олег\\OneDrive\\Рабочий стол\\cases_auto\\wb_project\\screen\\" + name_screenshot)

    # Метод проверки по url

    def assert_url(self, result):
        get_url = self.driver_g.current_url
        assert get_url == result
        print("Проверка по url прошла успешно")