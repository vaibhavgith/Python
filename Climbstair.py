# Climbstair

class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [1,1]
        for i in range(2,n+1):
            arr.append(arr[i-2]+arr[i-1])
        return arr[n]
    
sol = Solution()
print(sol.climbStairs(3))
    

# ==========================================================================

# Remove Duplicates from Sorted List 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:  # Handle the edge case of an empty list
            return None
        
        current = head  # Start traversal from the head of the list
        while current and current.next:
            if current.val == current.next.val:  # Check for duplicate
                current.next = current.next.next  # Skip the duplicate node
            else:
                current = current.next  # Move to the next distinct node
        
        return head  # Return the modified list     

#  Annother solution using SET()
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None
        unique_val = set()
        dummy = ListNode(0)
        current = dummy
        while head:
            if head.val not in unique_val:
                unique_val.add(head.val)
                current.next = ListNode(head.val)
                current = current.next
            head = head.next
        return dummy.next
# =================================================================================

class Solution(object):
    def merge(self, nums1, m, nums2, n):
      for j in range(n):
          nums1[m+j] = nums2[j]
      nums1.sort()

# Using two pointers
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = m - 1
        j = n - 1
        k = m + n - 1
        
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1



        