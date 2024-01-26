from Library.read_excel import ReadExcel

class addtocart:

    rd = ReadExcel()
    lo = rd.locators_details()


    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, u_name):
        # if isinstance(u_name, float):
        #     u_name = str(int(u_name))
            locator = self.lo["uname"]
            print(*locator)
            self.driver.find_element(*locator).send_keys(u_name)

    def enter_pswd(self, pswd):
        # if isinstance(pswd, float):
        #     pswd = str(int(pswd))
            locator = self.lo["password"]
            self.driver.find_element(*locator).send_keys(pswd)

    def click_on_login(self):
        locator = self.lo["login"]
        self.driver.find_element(*locator).click()

    def click_on_add_to_cart(self):
        locators = self.lo["add_to_cart"]
        self.driver.find_element(*locators).click()
