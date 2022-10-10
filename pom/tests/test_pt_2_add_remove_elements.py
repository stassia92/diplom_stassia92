import pytest
import allure
from diploma.pom.pages.diplom_page_main import DiplomPageMain


@allure.suite('Добавление элемента')
@allure.feature('Проверка добавления элемента на странице')
@pytest.mark.usefixtures('text_inside_test')
@pytest.mark.diplom
def test_7_add_element(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPageMain(driver)
        diplom_page.open()
        with allure.step('Переход на страницу примера добавления и удаления элементов'):
            diplom_page.open_add_remove_example()
        with allure.step('Добавление элемента на странице'):
            diplom_page.add_element_btn_click()
        assert diplom_page.element_delete_is_displayed()


@allure.suite('Удаление элемента')
@allure.feature('Проверка удаления элемента на странице')
@pytest.mark.usefixtures('text_inside_test')
def test_8_delete_element(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPageMain(driver)
        diplom_page.open()
        with allure.step('Переход на страницу примера добавления и удаления элементов'):
            diplom_page.open_add_remove_example()
        with allure.step('Добавление элемента на странице'):
            diplom_page.add_element_btn_click()
        with allure.step('Удаление элемента на странице'):
            diplom_page.remove_btn_click()
        assert diplom_page.element_delete_visible() is False
