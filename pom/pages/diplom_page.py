from diploma.pom.pages.base_page import BasePage
from diploma.pom.pages.locators import diplom_locators as dl


class DiplomPage(BasePage):
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
