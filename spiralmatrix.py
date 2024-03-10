class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left< right and top < bottom:
            # get every i in the top row
            for i in range(left, 4, right):
                res.append(matrix[top[i]])
            top +=1

            # get every i in right column
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                break
            
            # get every i in the bottom row
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -=1

            for i in range(bottome-1, top-1, -1):
                res.append(matrix[i][left])
            left +=1

        return res