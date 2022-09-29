from selenium.webdriver.support.select import Select
from diplom_stassia92.pom.pages.base_page import BasePage
from diplom_stassia92.pom.pages.locators import diplom_locators as dl


class DiplomPage2(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        return self.driver.get('https://the-internet.herokuapp.com/')

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

    # def context_menu_click(self):
    #     return self.find_element(dl.context_menu).click()
    #
    # def right_click_spot(self):
    #     return self.find_element(dl.right_click_spot).send_keys(Keys.SHIFT+Keys.F10)

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

    # def drag_and_drop_click(self):
    #     return self.find_element(dl.drag_and_drop_example).click()

    # def drag_and_drop(self):
    #     source_element = self.driver.find_element(dl.a_example)
    #     target_element = self.driver.find_element(dl.b_example)
    #     action = ActionChains(self.driver)
    #     action.drag_and_drop(source_element, target_element)
    #     return action.perform()
    #
    # def download_file(self):
    #     self.find_element(dl.download_file).click()
    #     return self.find_element(dl.example_download).click()
    #
    # def file_check(self):
    #     self.file = Path('test.txt')
    #     if self.file.exists():
    #         print("True")
    #     else:
    #         print("False")

    def entry_ad(self):
        return self.find_element(dl.entry_ad).click()

    def close_entry_ad(self):
        return self.find_element(dl.ad_close).click()

    def ad_window_is_displayed(self):
        return self.find_element(dl.ad_win).is_displayed()

    def upload_file_click(self):
        return self.find_element(dl.file_upload).click()