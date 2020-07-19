import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver


class HelloWorld(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path = r'./chromedriver.exe')
        driver = cls.driver
        driver.implicitly_wait(10)

    def test_hello_world(self):
        driver = self.driver
        driver.get('http://www.platzi.com')
        
    def test_visit_wikipedia(self):
        self.driver.get('http://www.wikipedia.org')

    @classmethod
    def tearDownClass(cls):
        return cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
