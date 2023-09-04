import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait

import frontend_case_analysis as fca

class FrontendTestCases(unittest.TestCase):
    """Tests for UI."""

    def setUp(self):
        self.service = Service('./chromedriver-win64/chromedriver.exe')
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.maximize_window()
        self.test_link = 'https://flights-app.pages.dev/'
        self.driver.get(self.test_link)
        self.cities = fca.return_cities_list(self.driver)
        self.driver.refresh()

    def test_not_same_value(self):
        self.driver.refresh()
        for i in self.cities:
            fca.write_from_side(self.driver, i)
            fca.write_to_side(self.driver, i)
            self.assertNotEqual(fca.read_from_side(self.driver), 
                    fca.read_to_side(self.driver))
        #ResourceWarning self.driver.exit()/quit()

    #def _helper(self):
        #pass

    def test_same_x(self):
        self.driver.refresh()
        for i in self.cities[:2]:
            for j in self.cities[5:]:
                if i != j:
                    self.assertEqual(
                            fca.count_by_text(self.driver, string1=i, string2=j),
                            fca.count_tables(self.driver, string1=i, string2=j))
        #ResourceWarning
        #self.driver.exit/quit çözmüyor


if __name__ == '__main__':
    unittest.main()