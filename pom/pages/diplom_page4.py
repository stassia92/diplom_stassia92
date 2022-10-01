from diploma.pom.pages.base_page import BasePage
from diploma.pom.pages.locators import diplom_locators as dl
import requests


class DiplomPage4(BasePage):

    def open(self):
        return self.driver.get('https://the-internet.herokuapp.com/')

    def status_code_200_example(self):
        self.find_element(dl.status_code_examples).click()
        return self.find_element(dl.code_200).click()

    @staticmethod
    def code_200_check():
        r = requests.get('https://the-internet.herokuapp.com/status_codes/200')
        return r.status_code == 200

    def status_code_301_example(self):
        self.find_element(dl.status_code_examples).click()
        return self.find_element(dl.code_301).click()

    @staticmethod
    def code_301_check():
        r = requests.get('https://the-internet.herokuapp.com/status_codes/301')
        return r.status_code == 301

    def status_code_404_example(self):
        self.find_element(dl.status_code_examples).click()
        return self.find_element(dl.code_404).click()

    @staticmethod
    def code_404_check():
        r = requests.get('https://the-internet.herokuapp.com/status_codes/404')
        return r.status_code == 404

    def status_code_500_example(self):
        self.find_element(dl.status_code_examples).click()
        return self.find_element(dl.code_500).click()

    @staticmethod
    def code_500_check():
        r = requests.get('https://the-internet.herokuapp.com/status_codes/500')
        return r.status_code == 500

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

    def nested_frame_txt(self):
        return self.find_element(dl.frames_body).text

    def bottom_frame(self):
        return self.driver.switch_to.frame('frame-bottom')

    def left_frame(self):
        self.driver.switch_to.frame("frame-top")
        return self.driver.switch_to.frame('frame-left')

    def middle_frame(self):
        self.driver.switch_to.frame("frame-top")
        return self.driver.switch_to.frame('frame-middle')

    def right_frame(self):
        self.driver.switch_to.frame("frame-top")
        return self.driver.switch_to.frame('frame-right')
