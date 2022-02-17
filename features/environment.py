from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

def before_scenario(context, scenario):
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service)
    # context.driver.implicitly_wait(10)
    context.driver.maximize_window()
    return context.driver
    # print('before' + scenario.name)


def after_scenario(context, scenario):
    pass
    context.driver.close()


def test():
    print('Before')
    yield
    print('tear down')