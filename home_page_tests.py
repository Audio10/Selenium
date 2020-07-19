"""Test class to use selenium."""
import unittest
from selenium import webdriver


class HomePageTests(unittest.TestCase):
    """Class to use the selenium driver """

    def setUp(self):
        """You need to put all the steps that need to complete before run any test_case """
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
        driver = self.driver
        driver.get("http://demo.onestepcheckout.com/")
        driver.maximize_window()
        driver.implicitly_wait(15)

    def test_search_text_field(self):
        """Test case to find a element by id """
        search_field = self.driver.find_element_by_id("search")

    def test_search_test_field_by_name(self):
        """Test case to find a element by name """
        search_field = self.driver.find_element_by_name("q")

    def test_search_text_field_class_name(self):
        """Test case to find a element by class_name """
        search_field = self.driver.find_element_by_class_name("input-text")

    def test_search_button_enabled(self):
        """Test case to find a element by class_name"""
        button = self.driver.find_element_by_class_name("button")

    def test_count_of_promo_banner_images(self):
        """Test case to find a nested element in this case we assert
        that this has a list of 3 elements"""
        banner_list = self.driver.find_element_by_class_name("promos")
        banners = banner_list.find_elements_by_tag_name("img")
        self.assertEqual(3, len(banners))

    def test_vip_promo(self):
        """Test case to find a element by xpath"""
        vip_promo = self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/header/div/a/img[1]")

    def test_shopping_cart(self):
        """Test case to find a element by css_selector"""
        shopping_cart_icon = self.driver.find_element_by_css_selector(
            "div.header-minicart span.icon")

    def tearDown(self):
        """Here we'll have all the things that will happend after ran all the test_cases """
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
