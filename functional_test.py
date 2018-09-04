from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.brower = webdriver.Firefox()

    def tearDown(self):
        self.brower.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 应用首页
        self.brower.get('http://localhost:8000')
        self.assertIn('To-Do', self.brower.title)
        header_text = self.brower.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # 待办事项
        inputbox = self.brower.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # 输入待办事项
        inputbox.send_keys('Buy peacoke feathers')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.brower.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(any(rows.text == '1: Buy peacoke feathers for now in rows'))

        self.fail('Finish the test')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
