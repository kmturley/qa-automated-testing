from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from behave import given, when, then
from qa.environment_variables import BASE_URL


@given('I am on "{uri}"')
def get(context, uri):
    if uri.lower() == 'index':
        context.driver.get(BASE_URL)
    else:
        context.driver.get(BASE_URL + uri)
