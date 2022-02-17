from pages.BasePage import BasePage
from pages.assistors import Assistors
from pages.locators import Loginlocators as loginLocators
from pages.locators import QAinterviewlocators as qaLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Login(BasePage,Assistors):

    def enter_username(self, username):
        user_name_input = self.driver.find_element_by_name(loginLocators.user_name_text)
        self.enter_text(element=user_name_input, value=username)
        # print("entered user name")

    def enter_password(self,password):
        password_input = self.driver.find_element_by_name(loginLocators.password_text)
        self.enter_text(element=password_input, value=password)
        # print("entered password")

    def click_login_button(self):
        login_button = self.driver.find_element_by_xpath(loginLocators.login_button)
        self.click_button(login_button)
        # print("clicked login button")

    def get_page_title(self):
        return self.driver.title

    def get_logged_in_text(self):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(qaLocators.logged_in_text))
        return element.text

