import pytest
import allure
from diploma.pom.pages.diplom_page_main import DiplomPageMain


@allure.suite('Заголовок сайта')
@allure.feature('Проверка корректности заголовка сайта')
@pytest.mark.usefixtures('print_text', 'text_inside_test')
@pytest.mark.diplom
def test_1_check_header_of_website(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPageMain(driver)
        diplom_page.open()
        assert "Welcome to the-internet" in diplom_page.header_txt()


@allure.suite('Заголовок примеров для автоматизации')
@allure.feature('Проверка корректности заголовка примеров на странице сайта')
@pytest.mark.usefixtures('text_inside_test')
def test_2_check_header_of_available_examples(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPageMain(driver)
        diplom_page.open()
        assert "Available Examples" in diplom_page.header_examples_txt()


@allure.suite('Текст в конце страницы сайта')
@allure.feature('Проверка корректности текста в конце страницы сайта')
@pytest.mark.usefixtures('text_inside_test')
def test_3_check_footer_main_page_of_website(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPageMain(driver)
        diplom_page.open()
        assert "Powered by Elemental Selenium" in diplom_page.main_page_footer_txt()


@allure.suite('Отображение кнопки перехода на гитхаб')
@allure.feature('Проверка отображения кнопки перехода на гитхаб автора сайта')
@pytest.mark.usefixtures('text_inside_test')
def test_4_check_github_btn_is_displayed(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPageMain(driver)
        diplom_page.open()
        assert diplom_page.github_btn_is_displayed()


@allure.suite('Переход на страницу гитхаб')
@allure.feature('Проверка перехода на гитхаб автора сайта')
@pytest.mark.usefixtures('text_inside_test')
def test_5_check_github_btn_transfer_to_github(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPageMain(driver)
        diplom_page.open()
    with allure.step('Нажатие кнопки перехода на гитхаб автора'):
        diplom_page.github_btn_click()
        assert diplom_page.url_check() == "https://github.com/saucelabs/the-internet" and \
               diplom_page.github_author_name_is_displayed()


@allure.suite('Наличие картинки на кнопке перехода на гитхаб')
@allure.feature('Проверка отображения изображения на кнопке перехода на гитхаб')
@pytest.mark.usefixtures('text_inside_test')
def test_6_check_github_btn_image(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPageMain(driver)
        diplom_page.open()
        assert diplom_page.github_btn_image_exist()
