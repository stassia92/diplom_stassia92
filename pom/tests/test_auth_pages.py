import pytest
import allure
from diploma.pom.pages.diplom_page_main import DiplomPageMain


@allure.suite('Простая авторизация')
@allure.feature('Проверка простой авторизации ')
@pytest.mark.usefixtures('text_inside_test')
def test_14_simple_auth_page(driver):
    with allure.step('Открытие сайта простой авторизации'):
        diplom_page = DiplomPageMain(driver)
        diplom_page.open()
    with allure.step('Переход на сайт авторизации с введенными данными'):
        diplom_page.simple_auth_page()
        assert "Congratulations! " \
               "You must have the proper credentials" in diplom_page.simple_auth_page()


@allure.suite('Авторизация')
@allure.feature('Проверка авторизации на странице')
@pytest.mark.usefixtures('text_inside_test')
@pytest.mark.diplom
def test_15_form_authentication_success(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPageMain(driver)
        diplom_page.open()
    with allure.step('Открытие страницы с примером Form Authentication'):
        diplom_page.form_authentication_click()
    with allure.step('Заполнение формы username'):
        diplom_page.username_field()
    with allure.step('Заполнение формы password'):
        diplom_page.password_field()
    with allure.step('Нажатие кнопки Login'):
        diplom_page.login_btn()
    assert "You logged into a secure area!" in diplom_page.login_success_txt()


@allure.suite('Авторизации с ошибкой в username')
@allure.feature('Проверка авторизации c ошибкой в username')
@pytest.mark.usefixtures('text_inside_test')
def test_16_form_authentication_wrong_username(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPageMain(driver)
        diplom_page.open()
    with allure.step('Открытие страницы с примером Form Authentication'):
        diplom_page.form_authentication_click()
    with allure.step('Заполнение формы username с ошибкой'):
        diplom_page.username_field_with_mistake()
    with allure.step('Заполнение формы password'):
        diplom_page.password_field()
    with allure.step('Нажатие кнопки Login'):
        diplom_page.login_btn()
    assert "Your username is invalid!" in diplom_page.login_success_txt()


@allure.suite('Авторизации с ошибкой в password')
@allure.feature('Проверка авторизации c ошибкой в password')
@pytest.mark.usefixtures('text_inside_test')
def test_17_form_authentication_wrong_password(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPageMain(driver)
        diplom_page.open()
    with allure.step('Открытие страницы с примером Form Authentication'):
        diplom_page.form_authentication_click()
    with allure.step('Заполнение формы username'):
        diplom_page.username_field()
    with allure.step('Заполнение формы password с ошибкой'):
        diplom_page.password_field_mistake()
    with allure.step('Нажатие кнопки Login'):
        diplom_page.login_btn()
    assert "Your password is invalid!" in diplom_page.login_success_txt()
