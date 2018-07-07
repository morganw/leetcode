#-*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/merge-two-sorted-lists/description/

将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2 
        if not l2:
            return l1 
        
        result = None
        merge_node = None
        while l1 and l2:
            if l1.val <= l2.val:
                new_node = l1 
                l1 = l1.next
            else:
                new_node = l2 
                l2 = l2.next
            if not merge_node:
                merge_node = new_node
            else:
                merge_node.next = new_node
                merge_node = new_node
            if not result:
                result = merge_node
        if l1:
            merge_node.next = l1 
        if l2:
            merge_node.next = l2 
 
        return result
        
    
l1 = ListNode(1)
l1_2 = ListNode(2)
l1.next = l1_2
l1_3 = ListNode(4)
l1_2.next = l1_3

l2 = ListNode(1)
l2_2 = ListNode(3)
l2.next = l2_2
l2_3 = ListNode(4)
l2_2.next = l2_3

s = Solution()
l = s.mergeTwoLists(l1, l2)
while l:
    print l.val
    l = l.next

    
    
    
    
    
    
    