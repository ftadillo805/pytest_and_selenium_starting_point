

class PageChecker:

    def __init__(self, page):
        self.__page = page
        self.__hard = True
        self.__soft_fails_count = 0
        self.__success_msg = None
        self.__fail_msg = None


    def __getattr__(self, attr_name):
        attr = getattr(self.__page, attr_name)
        return self.__encapsulate_page_attr(attr)


    def __encapsulate_page_attr(self, attr):
        def encapsulated_page_attr():
            value = attr() if callable(attr) else attr
            success_message = self.__success_msg
            fail_message = self.__fail_msg

            # Reset the message member variables.
            self.__success_msg = None
            self.__fail_msg = None

            if self.__hard:
                assert value, fail_message
                print(success_message)
            
            else:
                if not value:
                    self.__soft_fails_count += 1
                    print(fail_message)

        return encapsulated_page_attr


    def _hard_mode(self, hard):
        self.__hard = hard
        return self


    def _success_message_for_next_check(message):
        self.__success_msg = message

    
    def _fail_message_for_next_check(message):
        self.__fail_msg = message


    def soft_fails_less_than(self, number):
        assert number < self.__soft_fails_count




class Page:

    def get_this(self):
        print('hello')
        return False


page = Page()

checker = PageChecker(page)

checker.get_this()