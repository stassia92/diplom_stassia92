import pytest
import allure
from diploma.pom.pages.diplom_page_main import DiplomPageMain


@allure.suite('Выключение чекбокса №2')
@allure.feature('Проверка на выключение чекбокса 2')
@pytest.mark.usefixtures('text_inside_test')
def test_9_turn_off_checkbox_2(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPageMain(driver)
        diplom_page.open()
    with allure.step('Переход на страницу с чекбоксами'):
        diplom_page.checkboxes_example_click()
    with allure.step('Выключение чекбокса №2'):
        diplom_page.checkbox_2_()
    with allure.step('Проверка выключенного чекбокса №2 '):
        diplom_page.checkbox_2_selected()
    assert diplom_page.checkbox_2_selected() is False


@allure.suite('Включение всех чекбоксов')
@allure.feature('Проверка включения всех чекбоксов на странице сайта')
@pytest.mark.usefixtures('text_inside_test')
@pytest.mark.diplom
def test_10_turn_on_all_checkboxes(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPageMain(driver)
        diplom_page.open()
    with allure.step('Открытие страницы примера с чекбоксами'):
        diplom_page.checkboxes_example_click()
    with allure.step('Выключение чекбокса №2'):
        diplom_page.checkbox_2_()
    with allure.step('Включение чекбокса №1'):
        diplom_page.checkbox_1_()
    with allure.step('Включение чекбокса №2'):
        diplom_page.checkbox_2_()
    assert diplom_page.checkbox_1_selected() and diplom_page.checkbox_2_selected()


@allure.suite('Выключение чекбокса №1')
@allure.feature('Проверка выключенного чекбокса №1')
@pytest.mark.usefixtures('text_inside_test')
def test_11_turn_off_checkbox_1(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPageMain(driver)
        diplom_page.open()
    with allure.step('Открытие страницы примера с чекбоксами'):
        diplom_page.checkboxes_example_click()
    with allure.step('Включение чекбокса №1'):
        diplom_page.checkbox_1_()
    with allure.step('Выключение чекбокса №1'):
        diplom_page.checkbox_1_()
    with allure.step('Проверка выключенного чекбокса №1 '):
        diplom_page.checkbox_1_selected()
    assert diplom_page.checkbox_1_selected() is False
