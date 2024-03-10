class Solution:
    def rotateImage(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead
        """
        l, r = 0, len(matrix) - 1
        
        while l < r:
            for i in range(r - 1):
                top, bottom = l, r

                # save the topleft
                topleft = matrix[top][1 + i]

                # move bottom left into top left
                matrix[top][1 + i] = matrix[bottom - i][1]

                # move bottom right into bottom left
                matrix[bottom - i][1] = matrix[bottom][r - i]

                matrix[bottom][r - i] = matrix[top + i][r]

                matrix[top + i][r] = topleft

            r -= 1
            l += 1

