import pytest
import allure
from diploma.pom.pages.diplom_page_main import DiplomPageMain


@allure.suite('Hover 1')
@allure.feature('Проверка наведения курсора на фото получение инфо о нем ')
@pytest.mark.usefixtures('text_inside_test')
@pytest.mark.diplom
def test_25_hover_1(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPageMain(driver)
        diplom_page.open()
    with allure.step('Открытие открытие примера Hovers'):
        diplom_page.hovers_open_page()
    with allure.step('Наведение курсора на изображение слева и получение инфо о нем'):
        diplom_page.move_to_hover_1()
    assert 'name: user1' in diplom_page.hidden_user1_txt()


@allure.suite('Hover 2')
@allure.feature('Проверка наведения курсора на фото получение инфо о нем ')
@pytest.mark.usefixtures('text_inside_test')
def test_26_hover_2(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPageMain(driver)
        diplom_page.open()
    with allure.step('Открытие открытие примера Hovers'):
        diplom_page.hovers_open_page()
    with allure.step('Наведение курсора на изображение в центре и получение инфо о нем'):
        diplom_page.move_to_hover_2()
    assert 'name: user2' in diplom_page.hidden_user2_txt()


@allure.suite('Hover 3')
@allure.feature('Проверка наведения курсора на фото получение инфо о нем ')
@pytest.mark.usefixtures('text_inside_test')
def test_27_hover_3(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPageMain(driver)
        diplom_page.open()
    with allure.step('Открытие открытие примера Hovers'):
        diplom_page.hovers_open_page()
    with allure.step('Наведение курсора на изображение справа и получение инфо о нем'):
        diplom_page.move_to_hover_3()
    assert 'name: user3' in diplom_page.hidden_user3_txt()
