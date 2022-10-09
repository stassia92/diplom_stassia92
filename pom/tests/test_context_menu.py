import pytest
import allure
from diploma.pom.pages.diplom_page_main import DiplomPageMain


@allure.suite('Контекстное меню')
@allure.feature('Проверка на появление алерта после вызова контекстного меню ')
@pytest.mark.usefixtures('text_inside_test')
def test_24_context_menu(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPageMain(driver)
        diplom_page.open()
        with allure.step('Открытие примера с Context Menu'):
            diplom_page.context_menu_example()
        with allure.step('Вызов контекстного меню с подтверждающим алертом'):
            diplom_page.context_menu()
    assert 'You selected a context menu' in diplom_page.alert_txt()
