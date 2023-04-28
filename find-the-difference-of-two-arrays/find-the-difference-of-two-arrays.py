class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1, s2 = set(nums1), set(nums2)

        result = [list(s1 - s2), list(s2 - s1)]

        return result

        for n in set(nums1):
            counter[n] += 1

        for n in set(nums2):
            counter[n] -= 1

        for num, c in counter.items():
            if c == 1:
                result[0].append(num)
            elif c == -1:
                result[1].append(num)

        return result