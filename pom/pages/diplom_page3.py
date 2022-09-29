from diplom_stassia92.pom.pages.base_page import BasePage
from diplom_stassia92.pom.pages.locators import diplom_locators as dl


class DiplomPage3(BasePage):

    def open(self):
        return self.driver.get('https://the-internet.herokuapp.com/')

    def choose_file_upload(self):
        self.find_element(dl.choose_file).send_keys('D:/diplom/puppy_and_kitty.jpg')
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

# def status_code_click(self):
#     self.find_element(dl.status_code_example).click()
#     return self.find_element(dl.code_200_example).click()
#
# def status_code_200(self):
#     status_200 = self.find_element(dl.code_200)
#     link_200 = status_200.get_attribute('href')
#     r = api.get(link_200)
#     if r.status_code == 200:
#         return True
#     else:
#         return False
