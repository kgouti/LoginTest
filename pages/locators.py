from selenium.webdriver.common.by import By


class Loginlocators:
    user_name_label = (By.XPATH, "//label[text()=\"Username\"]")
    user_name_text = "loginUsername"
    password_text = "loginPassword"
    login_button = "//button[text()=\"Login\"]"


class QAinterviewlocators:
    logged_in_text = "logged-in__success"
