from time import sleep
import pytest
import allure
from diploma.pom.pages.diplom_page import DiplomPage
from diploma.pom.pages.diplom_page2 import DiplomPage2
from diploma.pom.pages.diplom_page3 import DiplomPage3
from diploma.pom.pages.diplom_page4 import DiplomPage4
from diploma.pom.pages.diplom_page5 import DiplomPage5


@allure.suite('Заголовок сайта')
@allure.feature('Проверка корректности заголовка сайта')
@pytest.mark.usefixtures('print_text', 'text_inside_test')
@pytest.mark.diplom
def test_1_check_header_of_website(driver):
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


@allure.suite('Отображение кнопки перехода на гитхаб')
@allure.feature('Проверка отображения кнопки перехода на гитхаб автора сайта')
@pytest.mark.usefixtures('text_inside_test')
def test_4_check_github_btn_is_displayed(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPage(driver)
        diplom_page.open()
        assert diplom_page.github_btn_is_displayed()


@allure.suite('Переход на страницу гитхаб')
@allure.feature('Проверка перехода на гитхаб автора сайта')
@pytest.mark.usefixtures('text_inside_test')
def test_5_check_github_btn_transfer_to_github(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPage(driver)
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
        diplom_page = DiplomPage(driver)
        diplom_page.open()
        assert diplom_page.github_btn_image_exist()


@allure.suite('Добавление элемента')
@allure.feature('Проверка добавления элемента на странице')
@pytest.mark.usefixtures('text_inside_test')
@pytest.mark.diplom
def test_7_add_element(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPage(driver)
        diplom_page.open()
        with allure.step('Переход на страницу примера добавления и удаления элементов'):
            diplom_page.open_add_remove_example()
        with allure.step('Добавление элемента на странице'):
            diplom_page.add_element_btn_click()
        assert diplom_page.element_delete_is_displayed()


def test_8_delete_element(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPage(driver)
        diplom_page.open()
        with allure.step('Переход на страницу примера добавления и удаления элементов'):
            diplom_page.open_add_remove_example()
        with allure.step('Добавление элемента на странице'):
            diplom_page.add_element_btn_click()
        with allure.step('Удаление элемента на странице'):
            diplom_page.remove_btn_click()
        assert diplom_page.element_delete_visible() is False


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
@pytest.mark.diplom
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
    assert diplom_page.checkbox_1_selected() and diplom_page.checkbox_2_selected()


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


@allure.suite('Выбор option 1 из списка')
@allure.feature('Проверка на выбор option 1 из списка ')
@pytest.mark.usefixtures('text_inside_test')
@pytest.mark.diplom
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


@allure.suite('Авторизация')
@allure.feature('Проверка авторизации на странице')
@pytest.mark.usefixtures('text_inside_test')
@pytest.mark.diplom
def test_15_form_authentication_success(driver):
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
def test_16_form_authentication_wrong_username(driver):
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
def test_17_form_authentication_wrong_password(driver):
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


@allure.suite('Добавление файла')
@allure.feature('Проверка добавления файла на страницу')
@pytest.mark.usefixtures('text_inside_test')
@pytest.mark.diplom
def test_18_file_uploader(driver):
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
def test_19_file_uploader(driver):
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
def test_20_dynamic_ctrl_remove_checkbox(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPage3(driver)
        diplom_page.open()
    with allure.step('Открытие примера с Dinamic controls и удаление чекбокса'):
        diplom_page.dinamic_ctrl_remove_checkbox()
    assert "It's gone!" in diplom_page.message_txt()


@allure.suite('Динамическая кнопка добавления чекбокса')
@allure.feature('Проверка добавления чекбокса со страницы - динамической кнопкой')
@pytest.mark.usefixtures('text_inside_test')
def test_21_dynamic_ctrl_remove_checkbox(driver):
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
def test_22_dynamic_ctrl_enable_btn(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPage3(driver)
        diplom_page.open()
    with allure.step('Открытие примера с Dinamic controls и нажатие кнопки Enable'):
        diplom_page.dinamic_ctrl_enable()
    assert "It's enabled!" in diplom_page.message_txt()


@allure.suite('Динамическая кнопка выключения')
@allure.feature('Проверка выключения динамической кнопки')
@pytest.mark.usefixtures('text_inside_test')
def test_23_dynamic_ctrl_disable_btn(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPage3(driver)
        diplom_page.open()
    with allure.step('Открытие примера с Dinamic controls и нажатие кнопки Enable'):
        diplom_page.dinamic_ctrl_enable()
        sleep(3)
    with allure.step('Нажатие кнопки Disable'):
        diplom_page.dinamic_ctrl_disable()
    assert "It's disabled!" in diplom_page.message_txt()


@allure.suite('Контекстное меню')
@allure.feature('Проверка на появление алерта после вызова контекстного меню ')
@pytest.mark.usefixtures('text_inside_test')
def test_24_context_menu(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPage3(driver)
        diplom_page.open()
        with allure.step('Открытие примера с Context Menu'):
            diplom_page.context_menu_example()
        with allure.step('Вызов контекстного меню с подтверждающим алертом'):
            diplom_page.context_menu()
    assert 'You selected a context menu' in diplom_page.alert_txt()


@allure.suite('Hover 1')
@allure.feature('Проверка наведения курсора на фото получение инфо о нем ')
@pytest.mark.usefixtures('text_inside_test')
@pytest.mark.diplom
def test_25_hover_1(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPage3(driver)
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
        diplom_page = DiplomPage3(driver)
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
        diplom_page = DiplomPage3(driver)
        diplom_page.open()
    with allure.step('Открытие открытие примера Hovers'):
        diplom_page.hovers_open_page()
    with allure.step('Наведение курсора на изображение справа и получение инфо о нем'):
        diplom_page.move_to_hover_3()
    assert 'name: user3' in diplom_page.hidden_user3_txt()


@allure.suite('Status code 200')
@allure.feature('Проверка что страница возвращает status code 200 ')
@pytest.mark.usefixtures('text_inside_test')
@pytest.mark.diplom
def test_28_status_code_200(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPage4(driver)
        diplom_page.open()
    with allure.step('Открытие примера Status code 200'):
        diplom_page.status_code_200_example()
    assert diplom_page.code_200_check()


@allure.suite('Status code 301')
@allure.feature('Проверка что страница возвращает status code 301 ')
@pytest.mark.usefixtures('text_inside_test')
def test_29_status_code_301(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPage4(driver)
        diplom_page.open()
    with allure.step('Открытие примера Status code 301'):
        diplom_page.status_code_301_example()
    assert diplom_page.code_301_check()


@allure.suite('Status code 404')
@allure.feature('Проверка что страница возвращает status code 404 ')
@pytest.mark.usefixtures('text_inside_test')
def test_30_status_code_404(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPage4(driver)
        diplom_page.open()
    with allure.step('Открытие примера Status code 404'):
        diplom_page.status_code_404_example()
    assert diplom_page.code_404_check()


@allure.suite('Status code 500')
@allure.feature('Проверка что страница возвращает status code 500 ')
@pytest.mark.usefixtures('text_inside_test')
def test_31_status_code_500(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPage4(driver)
        diplom_page.open()
    with allure.step('Открытие примера Status code 500'):
        diplom_page.status_code_500_example()
    assert diplom_page.code_500_check()


@allure.suite('Frame iframe')
@allure.feature('Проверка перехода на iframe и отображения старого текста на странице  ')
@pytest.mark.usefixtures('text_inside_test')
@pytest.mark.diplom
def test_32_iframe_check_old_txt(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPage4(driver)
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
        diplom_page = DiplomPage4(driver)
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


@allure.suite('Nested frame bottom ')
@allure.feature('Переход на nested frame bottom и проверка текста внутри него')
@pytest.mark.usefixtures('text_inside_test')
def test_34_nested_frame_bottom(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPage4(driver)
        diplom_page.open()
    with allure.step('Открытие примера Frames '):
        diplom_page.frames_examples()
    with allure.step('Открытие примера Nested Frames '):
        diplom_page.nested_frames_examples()
    with allure.step('Переключение на nested frame bottom'):
        diplom_page.bottom_frame()
    assert 'BOTTOM' in diplom_page.nested_frame_txt()


@allure.suite('Nested frame left')
@allure.feature('Переход на nested frame left и проверка текста внутри него')
@pytest.mark.usefixtures('text_inside_test')
def test_35_nested_frame_bottom(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPage4(driver)
        diplom_page.open()
    with allure.step('Открытие примера Frames '):
        diplom_page.frames_examples()
    with allure.step('Открытие примера Nested Frames '):
        diplom_page.nested_frames_examples()
    with allure.step('Переключение на nested frame left'):
        diplom_page.left_frame()
    assert 'LEFT' in diplom_page.nested_frame_txt()


@allure.suite('Nested frame middle')
@allure.feature('Переход на nested frame middle и проверка текста внутри него')
@pytest.mark.usefixtures('text_inside_test')
def test_36_nested_frame_bottom(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPage4(driver)
        diplom_page.open()
    with allure.step('Открытие примера Frames '):
        diplom_page.frames_examples()
    with allure.step('Открытие примера Nested Frames '):
        diplom_page.nested_frames_examples()
        diplom_page = DiplomPage5(driver)
    with allure.step('Переключение на nested frame middle'):
        diplom_page.middle_frame()
    assert 'MIDDLE' in diplom_page.nested_frame_txt()


@allure.suite('Nested frame right')
@allure.feature('Переход на nested frame right и проверка текста внутри него')
@pytest.mark.usefixtures('text_inside_test')
@pytest.mark.diplom
def test_37_nested_frame_bottom(driver):
    with allure.step('Открытие главной страницы сайта'):
        diplom_page = DiplomPage4(driver)
        diplom_page.open()
    with allure.step('Открытие примера Frames '):
        diplom_page.frames_examples()
    with allure.step('Открытие примера Nested Frames '):
        diplom_page.nested_frames_examples()
        diplom_page = DiplomPage5(driver)
    with allure.step('Переключение на nested frame right'):
        diplom_page.right_frame()
    assert 'RIGHT' in diplom_page.nested_frame_txt()
