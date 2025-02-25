lass Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        y = m-1
        x = 0
        while x < n and y >= 0:
            if matrix[y][x] == target:
                return True
            elif matrix[y][x] < target:
                x += 1
            else:
                y -= 1
        return False