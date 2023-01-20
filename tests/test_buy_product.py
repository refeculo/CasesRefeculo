from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.assorty_page import Assorty_page
from pages.main_page import Main_page
from pages.model_page import Model_page
from pages.smart_chasov_page import Smart_chasov_page


def test_buy_product(set_up):
    """Вход в браузер"""
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('C:\\Users\\Олег\\OneDrive\\Рабочий стол\\cases_auto\\wb_project\\utilities\\chromedriver.exe')
    driver_g = webdriver.Chrome(options=options, service=g)

    main_page = Main_page(driver_g)
    main_page.select_menu()

    stp = Smart_chasov_page(driver_g)
    stp.pick_up_model_smart_chasov()

    ap = Assorty_page(driver_g)
    ap.select_open_model()

    mp = Model_page(driver_g)
    mp.buy_model()


    driver_g.quit()