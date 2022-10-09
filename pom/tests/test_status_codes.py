import pytest
import allure
from diploma.pom.pages.diplom_page_main import DiplomPageMain


@allure.suite('Status code 200')
@allure.feature('Проверка что страница возвращает status code 200 ')
@pytest.mark.usefixtures('text_inside_test')
@pytest.mark.diplom
def test_28_status_code_200(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPageMain(driver)
        diplom_page.open()
    with allure.step('Открытие примера Status code 200'):
        diplom_page.status_code_200_example()
    assert diplom_page.code_200_check()


@allure.suite('Status code 301')
@allure.feature('Проверка что страница возвращает status code 301 ')
@pytest.mark.usefixtures('text_inside_test')
def test_29_status_code_301(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPageMain(driver)
        diplom_page.open()
    with allure.step('Открытие примера Status code 301'):
        diplom_page.status_code_301_example()
    assert diplom_page.code_301_check()


@allure.suite('Status code 404')
@allure.feature('Проверка что страница возвращает status code 404 ')
@pytest.mark.usefixtures('text_inside_test')
def test_30_status_code_404(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPageMain(driver)
        diplom_page.open()
    with allure.step('Открытие примера Status code 404'):
        diplom_page.status_code_404_example()
    assert diplom_page.code_404_check()


@allure.suite('Status code 500')
@allure.feature('Проверка что страница возвращает status code 500 ')
@pytest.mark.usefixtures('text_inside_test')
def test_31_status_code_500(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPageMain(driver)
        diplom_page.open()
    with allure.step('Открытие примера Status code 500'):
        diplom_page.status_code_500_example()
    assert diplom_page.code_500_check()
