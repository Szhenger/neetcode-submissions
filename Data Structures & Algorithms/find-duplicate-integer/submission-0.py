class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Get slow and fast pointers
        slow = fast = 0
        # Floyd's Cycle Detection Algorithm (Part 1)
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # Floyd's Cycle Detection Algorithm (Part 2)
        temp = 0
        while True:
            slow = nums[slow]
            temp = nums[temp]
            if slow == temp:
                return slow
        
            