import datetime

import pytest

from Library.configure import Configuration
from Library.read_excel import ReadExcel

from POM.add_item_to_cart import addtocart


class Testaddtocart:

    td = ReadExcel()
    data = td.login_details()

    @pytest.mark.parametrize("u_name, pswd", data)
    def test_msg(self, u_name, pswd, init_driver):
        driver = init_driver
        try:
            n = addtocart(init_driver)
            n.enter_username(u_name)
            n.enter_pswd(pswd)
            n.click_on_login()
            n.click_on_add_to_cart()

        except BaseException as msg:
            td = datetime.datetime.now()
            name = f"screenshot_{td.date()}_{td.hour}_{td.minute}_{td.second}.png"
            driver.save_screenshot(Configuration.SCREENSHOT_PATH+name)
            raise msg
