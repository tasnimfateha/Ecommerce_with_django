import urllib
from urllib.parse import urljoin
from behave import given, when, then
from selenium import webdriver

@given("we want to search for a product")
def user_on_homepage(context):
    context.browser = webdriver.Chrome()
    context.browser.get('https://cobaltmonica-changerover-8000.codio-box.uk/')

@when("we enter {search_term} in the search field")
def user_fills_in_the_form(context, search_term):
    search_textfield = context.browser.find_element_by_name('search')
    search_textfield.send_keys(search_term)

@when("we submit the search form")
def user_submits_the_search_form(context):
    context.browser.find_element_by_name('submit').click()

@then("we see a list of products containing {search_term}")
def products_contain_search_term(context, search_term):
    assert search_term in context.browser.page_source


