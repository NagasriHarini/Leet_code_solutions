# Best Time to Buy and Sell Stock

## Problem Statement

You are given an array `prices` where `prices[i]` is the price of a stock on the `i-th` day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve. If no profit can be achieved, return `0`.

## Examples

### Example 1

```text
Input: prices = [7,1,5,3,6,4]
Output: 5
```

Explanation:

Buy on day 2 at price `1` and sell on day 5 at price `6`.

Profit = `6 - 1 = 5`

### Example 2

```text
Input: prices = [7,6,4,3,1]
Output: 0
```

Explanation:

No profitable transaction is possible.

## Constraints

```text
1 <= prices.length <= 10^5
0 <= prices[i] <= 10^4
```
