class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        tmp = nums[::]
        k = 0
        for i, n in enumerate(tmp):
            if n != val:
                nums[k] = n
                k += 1

        return k