import pytest, os, sys

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
"""
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
"""
import frontend_case_analysis as fca

class TestFrontendCases:
    """Tests for UI."""

    @pytest.fixture(scope="function")
    def driver_setup(self):
        #print("setup_method+")
        self.service = Service('./chromedriver-win64/chromedriver.exe')
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.maximize_window()
        self.test_link = 'https://flights-app.pages.dev/'
        self.driver.get(self.test_link)
        self.cities = fca.return_cities_list(self.driver)
        self.driver.refresh()

        if not os.path.exists("./res"):
            os.mkdir("./res")
        else:
            for file in os.listdir("./res"):
                file_path = os.path.join("./res", file)
                os.remove(file_path)
        #print("setup_method.")

        yield self.driver

        self.driver.quit()

    @pytest.fixture(scope="function")
    def teardown_method(self, request):
        #error = sys.exc_info()
        print("s._t", request.node.name)
        print("s._t2", request.node.originalname )
        print("sys[0]", sys.exc_info()[0])
        print("sys[1]", sys.exc_info()[1])
        print("sys[2]", sys.exc_info()[2])
        if sys.exc_info()[0]:
            test_method_name = request.node.name
            self.driver.save_screenshot(f"./res/{test_method_name}.png")
        #self.driver.quit()
        self.driver.refresh()


    def test_not_same_value(self, driver_setup, teardown_method):
        #print("test_not_same_value+")
        #self.driver.refresh()
        for i in self.cities:
            fca.write_from_side(self.driver, i)
            fca.write_to_side(self.driver, i)
            assert fca.read_from_side(self.driver) != fca.read_to_side(self.driver)
        #ResourceWarning self.driver.exit()/quit()
        #self.driver.quit()
        #print("test_not_same_value.")


    def test_same_x(self, driver_setup, teardown_method):
        #print("test_same_x.")
        #self.driver.refresh()
        for i in self.cities[:3]:
            for j in self.cities[-3:]:
                if i != j:
                    assert fca.count_by_text(self.driver, string1=i, string2=j) \
                            == fca.count_tables(self.driver, string1=i, string2=j)
        #ResourceWarning
        #self.driver.exit/quit çözmüyor
