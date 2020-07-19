import unittest
from selenium import webdriver


class BaseTestCase(unittest.TestCase):

    def setUp(self, url=None):
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        if url:
            print(url)
            driver.get('{}'.format(url))
        else:
            driver.get('http://demo.onestepcheckout.com/')

    def tearDown(self):
        self.driver.quit()
