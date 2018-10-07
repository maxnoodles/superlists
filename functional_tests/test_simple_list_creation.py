from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest
MAX_WAIT = 10


class NewVisitorTest(FunctionalTest):

    def test_can_start_a_list_for_one_user(self):
        # 伊丽丝进入首页，创建了2个待办事项
        # 应用首页
        self.browser.get(self.live_server_url)
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # 待办事项
        inputbox = self.get_item_input_box()
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # 输入待办事项
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        inputbox = self.get_item_input_box()
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # 伊丽丝新建一个待办事项清单
        self.browser.get(self.live_server_url)
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')

        # 现在轮到弗朗西斯的新用户访问网站
        ## 我们使用一个新的浏览器会话，确保信息不回从cookier中泄露出去
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # 弗朗西斯访问首页，看不到伊丽丝的事项
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # 弗朗西斯创建一个新的待办事项
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # 弗朗西斯获得了他自己的Url
        francrs_list_url = self.browser.current_url
        self.assertRegex(francrs_list_url, '/lists/.+')
        self.assertNotEqual(francrs_list_url, edith_list_url)

        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)