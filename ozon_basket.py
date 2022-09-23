import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def driver_init():
    options = webdriver.ChromeOptions()
    options.add_argument('chrome')
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.ozon.ru/")
    yield driver
    driver.close()

def wait_of_element_located(xpath, driver_init):
    element = WebDriverWait(driver_init, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, xpath)
        )
    )
    return element


def search_product(product_name,driver_init):
    input_product_name = wait_of_element_located(xpath='//*[@id="stickyHeader"]/div[3]/div/div[1]/form/div[1]/div[2]/input[1]',driver_init=driver_init)

    input_product_name.send_keys(product_name)
    input_product_name.send_keys(Keys.RETURN)

def add_product(driver_init):
    item_name = wait_of_element_located(xpath='//*[@id="layoutPage"]/div[1]/div[2]/div[2]/div[2]/div[4]/div[1]/div/div/div[1]/div[2]/div/a/span/span', driver_init=driver_init)
    add_button = wait_of_element_located(xpath='//*[@id="layoutPage"]/div[1]/div[2]/div[2]/div[2]/div[4]/div[1]/div/div/div[1]/div[3]/div[3]/div/div/div/button/span/span', driver_init=driver_init)
    add_button.click()
    return item_name.text

def open_basket(driver_init):
    basket_icon = wait_of_element_located(xpath='//*[@id="stickyHeader"]/div['
                                                '4]/a[2]/svg', driver_init=driver_init)
    item_name = wait_of_element_located(xpath='//*[@id="layoutPage"]/div['
                                              '1]/div/div/div[3]/div[4]/div['
                                              '1]/div[1]/div/div[2]/div['
                                              '2]/div[1]/div/div/div/div[2]/a/span[1]/span',driver_init=driver_init)
    basket_icon.click()
    return item_name.text



def test_ozon_basket(driver_init):

    search_product("телевизор lg", driver_init=driver_init)
    add_product(driver_init=driver_init)
    open_basket(driver_init=driver_init)
    item_name_in_search_list = add_product(driver_init=driver_init)
    item_name_in_basket = open_basket(driver_init=driver_init)
    assert item_name_in_basket == item_name_in_search_list


