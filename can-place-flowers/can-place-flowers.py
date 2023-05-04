class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        k = 0
        l = len(flowerbed)

        for i in range(l):
            if flowerbed[i] == 0:
                if i > 0 and flowerbed[i - 1] == 1:
                    continue
                if i < l - 1 and flowerbed[i + 1] == 1:
                    continue
                k += 1
                flowerbed[i] = 1

        return k >= n