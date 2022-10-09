import pytest
import allure
from diploma.pom.pages.diplom_page_main import DiplomPageMain


@allure.suite('Nested frame bottom ')
@allure.feature('Переход на nested frame bottom и проверка текста внутри него')
@pytest.mark.usefixtures('text_inside_test')
def test_34_nested_frame_bottom(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPageMain(driver)
        diplom_page.open()
    with allure.step('Открытие примера Frames '):
        diplom_page.frames_examples()
    with allure.step('Открытие примера Nested Frames '):
        diplom_page.nested_frames_examples()
    with allure.step('Переключение на nested frame bottom'):
        diplom_page.bottom_frame()
    assert 'BOTTOM' in diplom_page.nested_frame_text()


@allure.suite('Nested frame left')
@allure.feature('Переход на nested frame left и проверка текста внутри него')
@pytest.mark.usefixtures('text_inside_test')
def test_35_nested_frame_bottom(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPageMain(driver)
        diplom_page.open()
    with allure.step('Открытие примера Frames '):
        diplom_page.frames_examples()
    with allure.step('Открытие примера Nested Frames '):
        diplom_page.nested_frames_examples()
    with allure.step('Переключение на nested frame left'):
        diplom_page.left_frame()
    assert 'LEFT' in diplom_page.nested_frame_text()


@allure.suite('Nested frame middle')
@allure.feature('Переход на nested frame middle и проверка текста внутри него')
@pytest.mark.usefixtures('text_inside_test')
def test_36_nested_frame_bottom(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPageMain(driver)
        diplom_page.open()
    with allure.step('Открытие примера Frames '):
        diplom_page.frames_examples()
    with allure.step('Открытие примера Nested Frames '):
        diplom_page.nested_frames_examples()
    with allure.step('Переключение на nested frame middle'):
        diplom_page.middle_frame()
    assert 'MIDDLE' in diplom_page.nested_frame_text()


@allure.suite('Nested frame right')
@allure.feature('Переход на nested frame right и проверка текста внутри него')
@pytest.mark.usefixtures('text_inside_test')
@pytest.mark.diplom
def test_37_nested_frame_bottom(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPageMain(driver)
        diplom_page.open()
    with allure.step('Открытие примера Frames '):
        diplom_page.frames_examples()
    with allure.step('Открытие примера Nested Frames '):
        diplom_page.nested_frames_examples()
    with allure.step('Переключение на nested frame right'):
        diplom_page.right_frame()
    assert 'RIGHT' in diplom_page.nested_frame_text()
