from pages.BasePage import BasePage


class Assistors:

    def enter_text(self, element, value):
        element.send_keys(value)

    def click_button(self,element):
        element.click()
