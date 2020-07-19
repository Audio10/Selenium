from base import BaseTestCase
import unittest
from selenium.webdriver.support.ui import Select


class LanguageOptions(BaseTestCase):

    def test_select_language(self):
        exp_options = ['English', 'French', 'German']
        act_options = []
        # Get a select
        select_language = Select(self.driver.find_element_by_id('select-language'))

        # You can count that.
        self.assertEqual(3, len(select_language.options))

        for option in select_language.options:
            act_options.append(option.text)

        # Compare the arrays.
        self.assertListEqual(exp_options, act_options)

        # Get the first element in the select
        self.assertEqual('English', select_language.first_selected_option.text)

        # Select a element by text
        select_language.select_by_visible_text('German')
        self.assertTrue('store=german' in self.driver.current_url)

        select_language = Select(self.driver.find_elements_by_id('select-language'))

        # Select for a index
        select_language.select_by_index(0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
