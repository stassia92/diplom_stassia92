from diploma.pom.pages.base_page import BasePage
from diploma.pom.pages.locators import diplom_locators as dl
from selenium.webdriver.common.action_chains import ActionChains


class DiplomPage3(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        return self.driver.get('https://the-internet.herokuapp.com/')

    def choose_file_upload(self):
        self.find_element(dl.choose_file).send_keys(r'D:\diplom2022\diploma\puppy_and_kitty.jpg')
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

    def dinamic_ctrl_add_checkbox(self):
        return self.find_element(dl.remove_and_add_btn).click()

    def dinamic_ctrl_enable(self):
        self.find_element(dl.dynamic_controls).click()
        return self.find_element(dl.enable_disable_btn).click()

    def dinamic_ctrl_disable(self):
        return self.find_element(dl.enable_disable_btn).click()

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
