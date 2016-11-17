__author__ = 'Pierre | pierre@jisson.com'


def is_item_in_list_a_in_list_b(list_a, list_b):
    """
    Check if one of the items given in list_a is present in list_b.

    :return:    True will be returned if one of the item in list_a is present in list_b
    """
    for item in list_a:
        if item in list_b:
            return True
    return False
