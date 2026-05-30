class Solution(object):
    def oddCells(self, m, n, indices):
        """
        :type m: int
        :type n: int
        :type indices: List[List[int]]
        :rtype: int
        """
        output = 0
        matrix = [[0] * n for i in range(m)]
        for i in range(len(indices)):
            for j in range(len(indices[i])):
                increment = indices[i][j]
                if j == 0:
                    for x in range(len(matrix[increment])):
                        matrix[increment][x] += 1
                else:
                    for x in range(m):
                        matrix[x][increment] += 1
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] % 2 == 1:
                    output += 1
        return output