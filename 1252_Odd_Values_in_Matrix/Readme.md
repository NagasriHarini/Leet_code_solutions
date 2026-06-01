# Cells with Odd Values in a Matrix

## Problem Statement

Given `m` and `n` which represent the dimensions of a matrix initialized with all zeros, and an array `indices` where `indices[i] = [ri, ci]`, increment all cells in row `ri` and column `ci` by 1.

Return the number of cells with odd values in the matrix after applying all the increments.

## Examples

### Example 1

Input:

```text
m = 2, n = 3, indices = [[0,1],[1,1]]
```

Output:

```text
6
```

### Example 2

Input:

```text
m = 2, n = 2, indices = [[1,1],[0,0]]
```

Output:

```text
0
```

## Constraints

```text
1 <= m, n <= 50
1 <= indices.length <= 100
0 <= ri < m
0 <= ci < n
```
