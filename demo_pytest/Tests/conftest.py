import pytest
from selenium import webdriver

from Library.configure import Configuration


@pytest.fixture(params=["edge"])
def init_driver(request):
    global driver
    browser = request.param

    if browser.lower() == "edge":
        driver = webdriver.Edge()

    # else:
    #     driver = webdriver.Edge(executable_path=Configuration.MSEDGE_PATH)

    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(Configuration.URL)
    yield driver
    driver.close()
