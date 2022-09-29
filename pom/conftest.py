import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='session')
def print_text():
    print('\nTesting loading\n')
    yield None
    print('\nEnd!\n')


@pytest.fixture(scope='function')
def text_inside_test():
    print('\nНачало проверки теста\n')
    yield None
    print('\nКонец проверки теста\n')


@pytest.fixture(scope='function')
def driver():
    serv = Service(executable_path=r'D:\diplom\chromedriver.exe')
    driver_chrome = webdriver.Chrome(service=serv)
    driver_chrome.maximize_window()
    driver_chrome.implicitly_wait(10)
    yield driver_chrome
    driver_chrome.quit()
