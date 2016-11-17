from django.test import TestCase

from django_simple_domain.utils import is_item_in_list_a_in_list_b

__author__ = 'Pierre | pierre@jisson.com'


class UtilsListAItemInListBTestCase(TestCase):
    """
    Test case for utils.is_item_in_list_a_in_list_b method.
    """

    default_list_b = ['abc', 'def', 'ghi']

    def test_no_item_in_list_a(self):
        """
        Testing with an empty list_a.
        """

        list_a = []
        result = is_item_in_list_a_in_list_b(list_a, self.default_list_b)
        self.assertEqual(result, False)

        list_b = []
        result = is_item_in_list_a_in_list_b(list_a, list_b)
        self.assertEqual(result, False)

    def test_no_item_in_list_b(self):
        """
        Testing with an empty list_b.
        """

        list_b = []

        list_a = self.default_list_b
        result = is_item_in_list_a_in_list_b(list_a, list_b)
        self.assertEqual(result, False)

        list_b = []
        result = is_item_in_list_a_in_list_b(list_a, list_b)
        self.assertEqual(result, False)

    def test_item_common_to_both_lists(self):
        """
        Testing common items present in both lists.
        """

        list_a = ['xyz', 'ghi']
        result = is_item_in_list_a_in_list_b(list_a, self.default_list_b)
        # 'ghi' is supposed to be found in list_b
        self.assertEqual(result, True)

        list_a = ['xyz', 'ghi', 'abc']
        # 'ghi' or 'abc' are supposed to be found in list_b
        result = is_item_in_list_a_in_list_b(list_a, self.default_list_b)
        self.assertEqual(result, True)

        list_a = ['xyz', 'abcd']
        # 'abc' in list_a is not a valid result. So False is expected
        result = is_item_in_list_a_in_list_b(list_a, self.default_list_b)
        self.assertEqual(result, False)
