from behave import given, when, then
from pages.LoginPage import Login


@given("login url is opened")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.login_page = Login(context.driver)
    context.login_page.open_url()


@when("user enters valid username {user} and password {password}")
def step_impl(context, user, password):
    """
    :param user: User name from gherkin inputs
    :param password: Password from gherkin inputs
    :type context: behave.runner.Context
    """
    # time.sleep(2)
    enter_user_credentials(context=context, user=user, password=password)


@when("clicks login button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.login_page.click_login_button()


@then("login is successful")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    # print("Page title {}".format(context.login_page.get_page_title()))
    assert context.login_page.get_logged_in_text().strip() == "Successfully logged in!"


@when("user enters invalid username {user} and password {password}")
def step_impl(context, user, password):
    """
    :param user: User name from gherkin inputs
    :param password: Password from gherkin inputs
    :type context: behave.runner.Context
    """
    enter_user_credentials(context, user=user, password=password)
    pass


def enter_user_credentials(context, user, password):
    context.login_page.enter_username(username=user)
    context.login_page.enter_password(password=password)


@then("login is unsuccessful")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    # ToDo: After implement unsuccessful login functionality, assert
    pass


@when("user clicks login button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.login_page.click_login_button()