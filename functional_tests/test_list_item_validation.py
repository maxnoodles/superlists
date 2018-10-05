from .base import FunctionalTest
from unittest import skip
MAX_WAIT = 10


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # 测试提交空列表错误，重新输入正确
        self.fail("write me!")