import pytest
import allure
from diploma.pom.pages.diplom_page_main import DiplomPageMain


@allure.suite('Выбор option 1 из списка')
@allure.feature('Проверка на выбор option 1 из списка ')
@pytest.mark.usefixtures('text_inside_test')
@pytest.mark.diplom
def test_12_dropdown_1(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPageMain(driver)
        diplom_page.open()
    with allure.step('Открытие страницы с примером dropdown'):
        diplom_page.dropdown_click()
    with allure.step('Выбор option 1 из списка'):
        diplom_page.dropdown_1_on()
    assert "Option 1" in diplom_page.option_1_txt_exist_on_page()


@allure.suite('Выбор option 2 из списка')
@allure.feature('Проверка на выбор option 2 из списка ')
@pytest.mark.usefixtures('text_inside_test')
def test_13_dropdown_2(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPageMain(driver)
        diplom_page.open()
    with allure.step('Открытие страницы с примером dropdown'):
        diplom_page.dropdown_click()
    with allure.step('Выбор option 1 из списка'):
        diplom_page.dropdown_2_on()
    assert "Option 2" in diplom_page.option_2_txt_exist_on_page()
