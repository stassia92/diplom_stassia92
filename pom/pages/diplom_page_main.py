from diploma.pom.pages.base_page import BasePage
from diploma.pom.pages.locators import diplom_locators as dl
import requests
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DiplomPageMain(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        return self.driver.get('https://the-internet.herokuapp.com/')

    def header_txt(self):
        return self.find_element(dl.header_web).text

    def header_examples_txt(self):
        return self.find_element(dl.header_examples).text

    def main_page_footer_txt(self):
        return self.find_element(dl.main_page_footer).text

    def url_check(self):
        return self.driver.current_url

    def github_author_name_is_displayed(self):
        return self.find_element(dl.github_name).is_displayed()

    def github_btn_is_displayed(self):
        return self.find_element(dl.github_btn).is_displayed()

    def github_btn_image_exist(self):
        return self.find_element(dl.github_btn_image).is_displayed()

    def github_btn_click(self):
        return self.find_element(dl.github_btn).click()

    def open_add_remove_example(self):
        return self.find_element(dl.add_and_remove).click()

    def add_element_btn_click(self):
        return self.find_element(dl.add_element_btn).click()

    def remove_btn_click(self):
        return self.find_element(dl.del_element_btn).click()

    def element_delete_is_displayed(self):
        return self.find_element(dl.elements).is_displayed()

    def element_delete_visible(self):
        return self.find_element(dl.elements).is_selected()

    def checkboxes_example_click(self):
        return self.find_element(dl.checkboxes).click()

    def checkbox_2_selected(self):
        return self.find_element(dl.checkbox_2).is_selected()

    def checkbox_1_(self):
        return self.find_element(dl.checkbox_1).click()

    def checkbox_2_(self):
        return self.find_element(dl.checkbox_2).click()

    def checkbox_1_selected(self):
        return self.find_element(dl.checkbox_1).is_selected()

    def dropdown_click(self):
        return self.find_element(dl.dropdown_example).click()

    def simple_auth_page(self):
        self.driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
        return self.find_element(dl.auth_log_in_txt).text

    def dropdown_1_on(self):
        elem = Select(self.find_element(dl.dropdown))
        return elem.select_by_index(1)

    def dropdown_2_on(self):
        elem = Select(self.find_element(dl.dropdown))
        return elem.select_by_index(2)

    def option_1_txt_exist_on_page(self):
        return self.find_element(dl.option_1_txt_on_page).text

    def option_2_txt_exist_on_page(self):
        return self.find_element(dl.option_2_txt_on_page).text

    def form_authentication_click(self):
        return self.find_element(dl.form_authentication).click()

    def username_field(self):
        self.find_element(dl.username).click()
        self.find_element(dl.username).send_keys('tomsmith')

    def username_field_with_mistake(self):
        self.find_element(dl.username).click()
        self.find_element(dl.username).send_keys('stassia92')

    def password_field(self):
        self.find_element(dl.password).click()
        return self.find_element(dl.password).send_keys('SuperSecretPassword!')

    def password_field_mistake(self):
        self.find_element(dl.password).click()
        return self.find_element(dl.password).send_keys('1234')

    def login_btn(self):
        return self.find_element(dl.login_btn).click()

    def login_success_txt(self):
        return self.find_element(dl.login_success).text

    def upload_file_click(self):
        return self.find_element(dl.file_upload).click()

    def middle_frame(self):
        self.driver.switch_to.frame("frame-top")
        return self.driver.switch_to.frame('frame-middle')

    def right_frame(self):
        self.driver.switch_to.frame("frame-top")
        return self.driver.switch_to.frame('frame-right')

    def nested_frame_txt(self):
        return self.find_element(dl.frames_body).text

    def choose_file_upload(self):
        self.find_element(dl.choose_file).send_keys(r'D:\diplom2022\diploma\test_data\lovely.jpg')
        return self.find_element(dl.upload_btn).click()

    def upl_btn_click(self):
        return self.find_element(dl.upload_btn).click()

    def upload_success_txt(self):
        return self.find_element(dl.upload_success_txt).text

    def error_if_send_no_file(self):
        return self.find_element(dl.error_if_file_not_uploaded).text

    def dinamic_ctrl_remove_checkbox(self):
        self.find_element(dl.dynamic_controls).click()
        self.find_element(dl.checkbox_dinamic).click()
        return self.find_element(dl.remove_and_add_btn).click()

    def message_txt(self):
        return self.find_element(dl.message).text

    def wait_click_btn(self):
        wait = WebDriverWait(self.driver, 30)
        wait = wait.until(EC.element_to_be_clickable(dl.remove_and_add_btn))
        wait.click()

    def dinamic_ctrl_enable(self):
        self.find_element(dl.dynamic_controls).click()
        return self.find_element(dl.enable_disable_btn).click()

    def wait_click_disable_btn(self):
        wait = WebDriverWait(self.driver, 30)
        wait = wait.until(EC.element_to_be_clickable(dl.enable_disable_btn))
        wait.click()

    def context_menu_example(self):
        return self.find_element(dl.context_menu).click()

    def context_menu(self):
        action = ActionChains(self.driver)
        element_locator = self.find_element(dl.right_click_spot)
        return action.context_click(element_locator).perform()

    def alert_txt(self):
        return self.driver.switch_to.alert.text

    def hovers_open_page(self):
        return self.find_element(dl.hovers_page).click()

    def move_to_hover_1(self):
        action = ActionChains(self.driver)
        element_locator = self.find_element(dl.hover_1)
        return action.move_to_element(element_locator).perform()

    def hidden_user1_txt(self):
        return self.find_element(dl.hidden_user1_txt).text

    def move_to_hover_2(self):
        action = ActionChains(self.driver)
        element_locator = self.find_element(dl.hover_2)
        return action.move_to_element(element_locator).perform()

    def hidden_user2_txt(self):
        return self.find_element(dl.hidden_user2_txt).text

    def move_to_hover_3(self):
        action = ActionChains(self.driver)
        element_locator = self.find_element(dl.hover_3)
        return action.move_to_element(element_locator).perform()

    def hidden_user3_txt(self):
        return self.find_element(dl.hidden_user3_txt).text

    def status_code_200_example(self):
        self.find_element(dl.status_code_examples).click()
        return self.find_element(dl.code_200).click()

    @staticmethod
    def code_200_check():
        request = requests.get('https://the-internet.herokuapp.com/status_codes/200')
        return request.status_code == 200

    def status_code_301_example(self):
        self.find_element(dl.status_code_examples).click()
        return self.find_element(dl.code_301).click()

    @staticmethod
    def code_301_check():
        request = requests.get('https://the-internet.herokuapp.com/status_codes/301')
        return request.status_code == 301

    def status_code_404_example(self):
        self.find_element(dl.status_code_examples).click()
        return self.find_element(dl.code_404).click()

    @staticmethod
    def code_404_check():
        request = requests.get('https://the-internet.herokuapp.com/status_codes/404')
        return request.status_code == 404

    def status_code_500_example(self):
        self.find_element(dl.status_code_examples).click()
        return self.find_element(dl.code_500).click()

    @staticmethod
    def code_500_check():
        request = requests.get('https://the-internet.herokuapp.com/status_codes/500')
        return request.status_code == 500

    def frames_examples(self):
        self.find_element(dl.frames_example).click()

    def iframe_example(self):
        return self.find_element(dl.iframe).click()

    def switch_to_iframe(self):
        return self.driver.switch_to.frame('mce_0_ifr')

    def old_txt_iframe_txt(self):
        return self.find_element(dl.iframe_txt).text

    def clear_iframe_form(self):
        return self.find_element(dl.iframe_txt).clear()

    def change_txt_iframe(self):
        return self.find_element(dl.iframe_txt).send_keys('Hello World!')

    def new_txt_iframe_txt(self):
        return self.find_element(dl.iframe_txt).text

    def nested_frames_examples(self):
        return self.find_element(dl.nested_frame_example).click()

    def bottom_frame(self):
        return self.driver.switch_to.frame('frame-bottom')

    def left_frame(self):
        self.driver.switch_to.frame("frame-top")
        return self.driver.switch_to.frame('frame-left')

    def nested_frame_text(self):
        return self.find_element(dl.frames_body).text
