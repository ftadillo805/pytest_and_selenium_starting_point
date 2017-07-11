from src import active_test_context
from src.page_checker import PageChecker

class Page:

    def __init__(self):
        self.__driver = active_test_context.driver
        self.__props = {}
        self.__page_checker = PageChecker(self)


    def get_url(self, url_key=''):
        if url_key:
            return self.__props.get(url_key, '')
        return self.__props.get('url', self.__props.get('URL', ''))


    def load(self):
        self.__driver.load(self.url)

    
    def hard_check(self, success_msg=None, fail_msg=None):
        self.__page_checker._hard_mode(True)
        if success_msg:
            self.__page_checker._success_message_for_next_check(success_msg)

        if fail_msg:
            self.__page_checker._fail_message_for_next_check(fail_msg)

        return self.__page_checker


    def soft_check(self, success_msg=None, fail_msg=None):
        return self.__page_checker._hard_mode(False)


    @property
    def url(self):
        return self.get_url()
