from diploma.pom.pages.base_page import BasePage
from diploma.pom.pages.locators import diplom_locators as dl



class DiplomPage5(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        return self.driver.get('https://the-internet.herokuapp.com/')

    def middle_frame(self):
        self.driver.switch_to.frame("frame-top")
        return self.driver.switch_to.frame('frame-middle')

    def right_frame(self):
        self.driver.switch_to.frame("frame-top")
        return self.driver.switch_to.frame('frame-right')

    def nested_frame_txt(self):
        return self.find_element(dl.frames_body).text
