class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        i, j = 0, len(matrix) - 1

        while i < j:
            for s in range(j - i):
                tmp = matrix[i][i + s]
                matrix[i][i + s] = matrix[j - s][i]
                matrix[j - s][i] = matrix[j][j - s]
                matrix[j][j - s] = matrix[i + s][j]
                matrix[i + s][j] = tmp

            i += 1
            j -= 1