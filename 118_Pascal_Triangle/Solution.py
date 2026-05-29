
def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    if numRows==1:
        return [[1]]

    table = [[1],[1,1]]
    if numRows==2:
        return table

    for i in range(2,numRows):
        row = []
        for j in range(0,i+1):
            if j==0 or j==i:
                row.append(1)

            else:
                row.append(table[i-1][j-1]+table[i-1][j])

        table.append(row)

    return table
            




        