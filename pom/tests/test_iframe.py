import pytest
import allure
from diploma.pom.pages.diplom_page_main import DiplomPageMain


@allure.suite('Frame iframe')
@allure.feature('Проверка перехода на iframe и отображения старого текста на странице  ')
@pytest.mark.usefixtures('text_inside_test')
@pytest.mark.diplom
def test_32_iframe_check_old_txt(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPageMain(driver)
        diplom_page.open()
    with allure.step('Открытие примера с Frames '):
        diplom_page.frames_examples()
    with allure.step('Открытие примера с iframe'):
        diplom_page.iframe_example()
    with allure.step('Переключение на iframe'):
        diplom_page.switch_to_iframe()
        assert diplom_page.old_txt_iframe_txt() == 'Your content goes here.'


@allure.suite('Frame iframe')
@allure.feature('Изменение текста в iframe и проверка на несовпадение нового текста со старым ')
@pytest.mark.usefixtures('text_inside_test')
def test_33_iframe_chech_new_txt(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPageMain(driver)
        diplom_page.open()
    with allure.step('Открытие примера с Frames '):
        diplom_page.frames_examples()
    with allure.step('Открытие примера с iframe'):
        diplom_page.iframe_example()
    with allure.step('Переключение на iframe'):
        diplom_page.switch_to_iframe()
    with allure.step('Очищение формы с текстом'):
        diplom_page.clear_iframe_form()
    with allure.step('Вписывание нового текста Hello world'):
        diplom_page.change_txt_iframe()
    assert diplom_page.new_txt_iframe_txt() != 'Your content goes here.'
