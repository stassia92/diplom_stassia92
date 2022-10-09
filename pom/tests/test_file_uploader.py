import pytest
import allure
from diploma.pom.pages.diplom_page_main import DiplomPageMain


@allure.suite('Добавление файла')
@allure.feature('Проверка добавления файла на страницу')
@pytest.mark.usefixtures('text_inside_test')
@pytest.mark.diplom
def test_18_file_uploader(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPageMain(driver)
        diplom_page.open()
    with allure.step('Открытие примера с File Uploader'):
        diplom_page.upload_file_click()
    with allure.step('Добавление файла и отправка'):
        diplom_page.choose_file_upload()
        assert 'File Uploaded!' in diplom_page.upload_success_txt()


@allure.suite('Отправление данных без файла')
@allure.feature('Проверка отправления пустых данных')
@pytest.mark.usefixtures('text_inside_test')
def test_19_file_uploader(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPageMain(driver)
        diplom_page.open()
    with allure.step('Открытие примера с File Uploader'):
        diplom_page.upload_file_click()
    with allure.step('Нажатие кнопки отправки файла'):
        diplom_page.upl_btn_click()
        assert 'Internal Server Error' in diplom_page.error_if_send_no_file()
