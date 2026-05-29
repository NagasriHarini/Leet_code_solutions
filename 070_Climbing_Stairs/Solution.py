
def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """

    if n==1:
        return 1 
    if n==2:
        return 2
    table = [0 for i in range(n)]
    table[0] = 1
    table[1] = 2
    for i in range(2,n):
        table[i] = table[i-1]+table[i-2]


    return table[n-1]

        