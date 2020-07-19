from base import BaseTestCase
import unittest
from selenium.webdriver.support.ui import WebDriverWait


class CompareProducts(BaseTestCase):

    def tests_compare_products_removal_alert(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()

        search_field.send_keys('tee')
        search_field.submit()

        driver.find_element_by_class_name('link-compare').click()
        driver.find_element_by_link_text('Clear All').click()

        alert = driver.switch_to_alert()
        alert_text = alert.text
        
        self.assertEqual('Are you sure you would like to remove all products from your comparison?', alert_text)

        alert.accept()
        #alert.dismiss() dismiss alert
        #alert.send_keys() write in the alert
        

if __name__ == "__main__":
    unittest.main(verbosity=2)