class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)

        answer = [1] * length
        left_prod = [1] * length
        left_prod[0] = nums[0]

        right_prod = [1] * length
        right_prod[-1] = nums[-1]

        for i in range(1, length):
            left_prod[i] = left_prod[i - 1] * nums[i]
            right_prod[length - 1 - i] = right_prod[length - i] * nums[length - 1 - i]

        for i in range(length):
            if i > 0:
                answer[i] *= left_prod[i - 1]
            if i < length - 1:
                answer[i] *= right_prod[i + 1]

        return answer