from base import BaseTestCase
import unittest
from time import sleep


class NavigationTest(BaseTestCase):

    def setUp(self):
        BaseTestCase.setUp(self, 'https://www.google.com/')

    def test_browser_navigation(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys('platzi')
        search_field.submit()

        # Return to the last page
        driver.back()
        sleep(3)

        # Move forward
        driver.forward()
        sleep(3)

        # Refresh the page
        driver.refresh()
        sleep(3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
