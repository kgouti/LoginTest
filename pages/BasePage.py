from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import Loginlocators as loginLocators


class BasePage(object):
    def __init__(self,driver):
        self.driver = driver
        pass

    def open_url(self):
        try:
            self.driver.get("https://login.dev.qa-experience.com")
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                loginLocators.user_name_label
            ))
        except TimeoutException:
            raise Exception("Unable to load page !")

