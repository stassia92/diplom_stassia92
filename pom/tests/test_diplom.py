from time import sleep
import pytest
import allure
from diplom_stassia92.pom.pages.diplom_page import DiplomPage
from diplom_stassia92.pom.pages.diplom_page2 import DiplomPage2
from diplom_stassia92.pom.pages.diplom_page3 import DiplomPage3


@allure.suite('Заголовок сайта')
@allure.feature('Проверка корректности заголовка сайта')
@pytest.mark.usefixtures('print_text', 'text_inside_test')
@pytest.mark.diplom
def test_1_check_of_header_website(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPage(driver)
        diplom_page.open()
        assert "Welcome to the-internet" in diplom_page.header_txt()


@allure.suite('Заголовок примеров для автоматизации')
@allure.feature('Проверка корректности заголовка примеров на странице сайта')
@pytest.mark.usefixtures('text_inside_test')
def test_2_check_header_of_available_examples(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPage(driver)
        diplom_page.open()
        assert "Available Examples" in diplom_page.header_examples_txt()


@allure.suite('Текст в конце страницы сайта')
@allure.feature('Проверка корректности текста в конце страницы сайта')
@pytest.mark.usefixtures('text_inside_test')
def test_3_check_footer_main_page_of_website(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPage(driver)
        diplom_page.open()
        assert "Powered by Elemental Selenium" in diplom_page.main_page_footer_txt()


@allure.suite('Открытие новой страницы')
@allure.feature('Проверка перехода на другую страницу сайта')
@pytest.mark.usefixtures('text_inside_test')
@pytest.mark.diplom
def test_4_check_open_new_page(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPage(driver)
        diplom_page.open()
    with allure.step('Переход на страницу A/B Testing'):
        diplom_page.open_ab_testing_page()
        assert diplom_page.url_check() == "https://the-internet.herokuapp.com/abtest"


@allure.suite('Отображение кнопки перехода на гитхаб')
@allure.feature('Проверка отображения кнопки перехода на гитхаб автора сайта')
@pytest.mark.usefixtures('text_inside_test')
def test_5_check_github_btn_is_displayed(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPage(driver)
        diplom_page.open()
        assert diplom_page.github_btn_is_displayed()


@allure.suite('Переход на страницу гитхаб')
@allure.feature('Проверка перехода на гитхаб автора сайта')
@pytest.mark.usefixtures('text_inside_test')
def test_6_check_github_btn_transfer_to_github(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPage(driver)
        diplom_page.open()
    with allure.step('Нажатие кнопки перехода на гитхаб автора'):
        diplom_page.github_btn_click()
        assert diplom_page.url_check() == "https://github.com/saucelabs/the-internet" and \
               diplom_page.github_author_name_is_displayed() is True


@allure.suite('Наличие картинки на кнопке перехода на гитхаб')
@allure.feature('Проверка отображения изображения на кнопке перехода на гитхаб')
@pytest.mark.usefixtures('text_inside_test')
def test_7_check_github_btn_image(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPage(driver)
        diplom_page.open()
        assert diplom_page.github_btn_image_exist()


@allure.suite('Добавление и удаление элемента')
@allure.feature('Проверка добавления и удаления элемента на странице')
@pytest.mark.usefixtures('text_inside_test')
def test_8_add_remove_elements(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPage(driver)
        diplom_page.open()
        with allure.step('Переход на страницу примера добавления и удаления элемента'):
            diplom_page.open_add_remove_example()
        with allure.step('Добавление элемента на странице'):
            diplom_page.add_element_btn_click()
        with allure.step('Удаление элемента на странице'):
            diplom_page.remove_btn_click()
        with allure.step('Проверка отображения кнопки Delete'):
            diplom_page.element_visible()
        assert diplom_page.element_visible() is False


@allure.suite('Простая авторизация')
@allure.feature('Проверка простой авторизации ')
@pytest.mark.usefixtures('text_inside_test')
def test_9_check_github_btn_image(driver):
    with allure.step('Открытие сайта простой авторизации'):
        diplom_page = DiplomPage2(driver)
        diplom_page.open()
    with allure.step('Переход на сайт авторизации с введенными данными'):
        diplom_page.simple_auth_page()
        assert "Congratulations! " \
               "You must have the proper credentials" in diplom_page.simple_auth_page()


@allure.suite('Выключение чекбокса №2')
@allure.feature('Проверка на выключение чекбокса 2')
@pytest.mark.usefixtures('text_inside_test')
def test_10_turn_off_checkbox_2(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPage(driver)
        diplom_page.open()
    with allure.step('Переход на страницу с чекбоксами'):
        diplom_page.checkboxes_example_click()
    with allure.step('Выключение чекбокса №2'):
        diplom_page.checkbox_2_()
    with allure.step('Проверка выключенного чекбокса №2 '):
        diplom_page.checkbox_2_selected()
    assert diplom_page.checkbox_2_selected() is False


@allure.suite('Включение всех чекбоксов')
@allure.feature('Проверка включения всех чекбоксов на странице сайта')
@pytest.mark.usefixtures('text_inside_test')
def test_11_turn_on_all_checkboxes(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPage(driver)
        diplom_page.open()
    with allure.step('Открытие страницы примера с чекбоксами'):
        diplom_page.checkboxes_example_click()
    with allure.step('Выключение чекбокса №2'):
        diplom_page.checkbox_2_()
    with allure.step('Включение чекбокса №1'):
        diplom_page.checkbox_1_()
    with allure.step('Включение чекбокса №2'):
        diplom_page.checkbox_2_()
    assert diplom_page.checkbox_1_selected() and diplom_page.checkbox_2_selected() is True


@allure.suite('Выключение чекбокса №1')
@allure.feature('Проверка включения всех чекбоксов на странице сайта')
@pytest.mark.usefixtures('text_inside_test')
def test_12_turn_off_checkbox_1(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPage(driver)
        diplom_page.open()
    with allure.step('Открытие страницы примера с чекбоксами'):
        diplom_page.checkboxes_example_click()
    with allure.step('Включение чекбокса №1'):
        diplom_page.checkbox_1_()
    with allure.step('Выключение чекбокса №1'):
        diplom_page.checkbox_1_()
    with allure.step('Проверка выключенного чекбокса №1 '):
        diplom_page.checkbox_1_selected()
    assert diplom_page.checkbox_1_selected() is False


# @allure.suite('Выключение чекбокса №1')
# @allure.feature('Проверка включения всех чекбоксов на странице сайта')
# @pytest.mark.usefixtures('text_inside_test')
# def test_13_drag_and_drop(driver):
#     with allure.step('Открытие главной страницы сайта'):
#         diplom_page = DiplomPage2(driver)
#         diplom_page.open()
#     with allure.step('Открытие страницы примера c drag and drop'):
#         diplom_page.drag_and_drop_click()
#         diplom_page.drag_and_drop()
#         sleep(3)


@allure.suite('Выбор option 1 из списка')
@allure.feature('Проверка на выбор option 1 из списка ')
@pytest.mark.usefixtures('text_inside_test')
def test_13_dropdown_1(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPage2(driver)
        diplom_page.open()
    with allure.step('Открытие страницы с примером dropdown'):
        diplom_page.dropdown_click()
    with allure.step('Выбор option 1 из списка'):
        diplom_page.dropdown_1_on()
    assert "Option 1" in diplom_page.option_1_txt_exist_on_page()


@allure.suite('Выбор option 2 из списка')
@allure.feature('Проверка на выбор option 2 из списка ')
@pytest.mark.usefixtures('text_inside_test')
def test_14_dropdown_2(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPage2(driver)
        diplom_page.open()
    with allure.step('Открытие страницы с примером dropdown'):
        diplom_page.dropdown_click()
    with allure.step('Выбор option 1 из списка'):
        diplom_page.dropdown_2_on()
    assert "Option 2" in diplom_page.option_2_txt_exist_on_page()


# @allure.suite('Выбор option 2 из списка')
# @allure.feature('Проверка на выбор option 2 из списка ')
# @pytest.mark.usefixtures('text_inside_test')
# def test_15_сontext_menu(driver):
#     with allure.step('Открытие главной страницы сайта'):
#         diplom_page = DiplomPage(driver)
#         diplom_page.open()
#         diplom_page.context_menu_click()
#         diplom_page.right_click_spot()
#         sleep(3)


@allure.suite('Выбор option 2 из списка')
@allure.feature('Проверка на выбор option 2 из списка ')
@pytest.mark.usefixtures('text_inside_test')
def test_15_dropdown_2(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPage2(driver)
        diplom_page.open()
    with allure.step('Открытие страницы с примером dropdown'):
        diplom_page.dropdown_click()
    with allure.step('Выбор option 1 из списка'):
        diplom_page.dropdown_2_on()
    assert "Option 2" in diplom_page.option_2_txt_exist_on_page()


@allure.suite('Авторизация')
@allure.feature('Проверка авторизации на странице')
@pytest.mark.usefixtures('text_inside_test')
def test_16_form_authentication_success(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPage2(driver)
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
def test_17_form_authentication_wrong_username(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPage2(driver)
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
def test_18_form_authentication_wrong_password(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPage2(driver)
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


# sleep
@allure.suite('Всплывающая реклама')
@allure.feature('Проверка на выключение всплывающей рекламы')
@pytest.mark.usefixtures('text_inside_test')
def test_19_entry_ad(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPage2(driver)
        diplom_page.open()
    with allure.step('Открытие страницы с примером Enty Ad'):
        diplom_page.entry_ad()
    with allure.step('Выключение всплывающей рекламы'):
        diplom_page.close_entry_ad()
        sleep(3)
    assert diplom_page.ad_window_is_displayed() is False


# @allure.suite('Авторизации с ошибкой в password')
# @allure.feature('Проверка авторизации c ошибкой в password')
# @pytest.mark.usefixtures('text_inside_test')
# def test_18_form_authentication_wrong_password(driver):
#     with allure.step('Открытие главной страницы сайта'):
#         diplom_page = DiplomPage2(driver)
#         diplom_page.open()
#         diplom_page.download_file()
#         sleep(5)
#         assert DiplomPage2.file_check() is "True"


@allure.suite('Добавление файла')
@allure.feature('Проверка добавления файла на страницу')
@pytest.mark.usefixtures('text_inside_test')
def test_20_file_uploader(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPage2(driver)
        diplom_page.open()
    with allure.step('Открытие примера с File Uploader'):
        diplom_page.upload_file_click()
    with allure.step('Добавление файла и отправка'):
        diplom_page = DiplomPage3(driver)
        diplom_page.choose_file_upload()
        assert 'File Uploaded!' in diplom_page.upload_success_txt()


@allure.suite('Отправление данных без файла')
@allure.feature('Проверка отправления пустых данных')
@pytest.mark.usefixtures('text_inside_test')
def test_21_file_uploader(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPage2(driver)
        diplom_page.open()
    with allure.step('Открытие примера с File Uploader'):
        diplom_page.upload_file_click()
    with allure.step('Нажатие кнопки отправки файла'):
        diplom_page = DiplomPage3(driver)
        diplom_page.upl_btn_click()
        assert 'Internal Server Error' in diplom_page.error_if_send_no_file()


@allure.suite('Динамическая кнопка удаления чекбокса')
@allure.feature('Проверка удаления чекбокса со страницы - динамической кнопкой')
@pytest.mark.usefixtures('text_inside_test')
def test_22_dynamic_ctrl_remove_checkbox(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPage3(driver)
        diplom_page.open()
    with allure.step('Открытие примера с Dinamic controls и удаление чекбокса'):
        diplom_page.dinamic_ctrl_remove_checkbox()
    assert "It's gone!" in diplom_page.message_txt()


# sleep
@allure.suite('Динамическая кнопка добавления чекбокса')
@allure.feature('Проверка добавления чекбокса со страницы - динамической кнопкой')
@pytest.mark.usefixtures('text_inside_test')
def test_23_dynamic_ctrl_remove_checkbox(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPage3(driver)
        diplom_page.open()
    with allure.step('Открытие примера с Dinamic controls и добавление чекбокса'):
        diplom_page.dinamic_ctrl_remove_checkbox()
        sleep(3)
        diplom_page.dinamic_ctrl_add_checkbox()
    assert "It's back!" in diplom_page.message_txt()


@allure.suite('Динамическая кнопка включения')
@allure.feature('Проверка включения динамической кнопки')
@pytest.mark.usefixtures('text_inside_test')
def test_24_dynamic_ctrl_enable_btn(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPage3(driver)
        diplom_page.open()
    with allure.step('Открытие примера с Dinamic controls и нажатие кнопки Enable'):
        diplom_page.dinamic_ctrl_enable()
    assert "It's enabled!" in diplom_page.message_txt()


@allure.suite('Динамическая кнопка выключения')
@allure.feature('Проверка выключения динамической кнопки')
@pytest.mark.usefixtures('text_inside_test')
def test_25_dynamic_ctrl_disable_btn(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPage3(driver)
        diplom_page.open()
    with allure.step('Открытие примера с Dinamic controls и нажатие кнопки Disable'):
        diplom_page.dinamic_ctrl_enable()
    assert "It's disabled!" in diplom_page.message_txt()

# @allure.suite('Динамическая кнопка выключения')
# @allure.feature('Проверка выключения динамической кнопки')
# @pytest.mark.usefixtures('text_inside_test')
# def test_25_dynamic_ctrl_disable_btn(driver):
#     with allure.step('Открытие главной страницы сайта'):
#         diplom_page = DiplomPage2(driver)
#         diplom_page.open()
#     with allure.step('Открытие примера с Dinamic controls и нажатие кнопки Disable'):
#         diplom_page.status_code_click()
#         diplom_page.status_code_200()
#         sleep(3)
#     assert diplom_page.status_code_200() is True
