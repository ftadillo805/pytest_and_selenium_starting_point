from selenium import webdriver


class AutomationDriver:

    def __init__(self, browser='firefox', **kwargs):
        remote_url = kwargs.pop('remote_url', '')
        if remote_url:
            self.__driver = webdriver.Remote(remote_url, **kwargs)

        elif browser == 'firefox':
            self.__driver = webdriver.Firefox(**kwargs)

        elif browser == 'chrome':
            self.__driver = webdriver.Chrome(**kwargs)

