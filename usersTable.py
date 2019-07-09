from tableElements import TableElements


class UsersTable(TableElements):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)

    def return_list(self):
        return super().return_list_of_names()