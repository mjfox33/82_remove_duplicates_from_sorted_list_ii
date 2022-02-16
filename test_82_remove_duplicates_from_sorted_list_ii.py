from code_82_remove_duplicates_from_sorted_list_ii import Solution
from code_82_remove_duplicates_from_sorted_list_ii import ListNode

def test_example_1():
    l7 = ListNode(5)
    l6 = ListNode(4, l7)
    l5 = ListNode(4, l6)
    l4 = ListNode(3, l5)
    l3 = ListNode(3, l4)
    l2 = ListNode(2, l3)
    head = ListNode(1, l2)
    result = ListNode(1, ListNode(2, ListNode(5, None)))
    s = Solution()

    assert s.deleteDuplicates(head) == result
