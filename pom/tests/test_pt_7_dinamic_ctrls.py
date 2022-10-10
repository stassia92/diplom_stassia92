import pytest
import allure
from diploma.pom.pages.diplom_page_main import DiplomPageMain


@allure.suite('Динамическая кнопка удаления чекбокса')
@allure.feature('Проверка удаления чекбокса со страницы - динамической кнопкой')
@pytest.mark.usefixtures('text_inside_test')
def test_20_dynamic_ctrl_remove_checkbox(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPageMain(driver)
        diplom_page.open()
    with allure.step('Открытие примера с Dinamic controls и удаление чекбокса'):
        diplom_page.dinamic_ctrl_remove_checkbox()
    assert "It's gone!" in diplom_page.message_txt()


@allure.suite('Динамическая кнопка добавления чекбокса')
@allure.feature('Проверка добавления чекбокса со страницы - динамической кнопкой')
@pytest.mark.usefixtures('text_inside_test')
def test_21_dynamic_ctrl_remove_checkbox(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPageMain(driver)
        diplom_page.open()
    with allure.step('Открытие примера с Dinamic controls и добавление чекбокса'):
        diplom_page.dinamic_ctrl_remove_checkbox()
        diplom_page.wait_click_btn()
    assert "It's back!" in diplom_page.message_txt()


@allure.suite('Динамическая кнопка включения')
@allure.feature('Проверка включения динамической кнопки')
@pytest.mark.usefixtures('text_inside_test')
def test_22_dynamic_ctrl_enable_btn(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPageMain(driver)
        diplom_page.open()
    with allure.step('Открытие примера с Dinamic controls и нажатие кнопки Enable'):
        diplom_page.dinamic_ctrl_enable()
    assert "It's enabled!" in diplom_page.message_txt()


@allure.suite('Динамическая кнопка выключения')
@allure.feature('Проверка выключения динамической кнопки')
@pytest.mark.usefixtures('text_inside_test')
def test_23_dynamic_ctrl_disable_btn(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPageMain(driver)
        diplom_page.open()
    with allure.step('Открытие примера с Dinamic controls и нажатие кнопки Enable'):
        diplom_page.dinamic_ctrl_enable()
    with allure.step('Нажатие кнопки Disable'):
        diplom_page.wait_click_disable_btn()
    assert "It's disabled!" in diplom_page.message_txt()
