from src import active_context

from selenium import webdriver


def pytest_runtest_setup(item):
    active_context.driver = webdriver.Firefox()


def pytest_runtest_teardown(item, nextitem):
    active_context.driver.quit()
