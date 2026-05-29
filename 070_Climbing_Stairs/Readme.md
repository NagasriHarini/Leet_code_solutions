# Climbing Stairs (LeetCode 70)

## Problem Statement

You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either:
- Climb 1 step
- Climb 2 steps

Return the number of distinct ways to reach the top.

---

## Example 1

### Input
```text
n = 2
```

### Output
```text
2
```

### Explanation
1. 1 + 1
2. 2

---

## Example 2

### Input
```text
n = 3
```

### Output
```text
3
```

### Explanation
1. 1 + 1 + 1
2. 1 + 2
3. 2 + 1

---

## Constraints

```text
1 <= n <= 45
```

---

## Key Observation

To reach step `n`:

- Come from step `n - 1` by taking 1 step.
- Come from step `n - 2` by taking 2 steps.

Therefore:

```text
ways(n) = ways(n - 1) + ways(n - 2)
```

This follows the Fibonacci sequence.

---

## Base Cases

```text
ways(1) = 1
ways(2) = 2
```

---

## Dry Run (n = 4)

```text
ways(1) = 1
ways(2) = 2
ways(3) = 3
ways(4) = 5
```

Possible ways:

```text
1+1+1+1
1+1+2
1+2+1
2+1+1
2+2
```

Answer:

```text
5
```

---

## Python Solution

```python
class Solution:
    def climbStairs(self, n):
        if n <= 2:
            return n

        first = 1
        second = 2

        for i in range(3, n + 1):
            current = first + second
            first = second
            second = current

        return second
```

---

## Time Complexity

```text
O(n)
```

## Space Complexity

```text
O(1)
```

---

## Why It Works

Every way to reach step `n` must come from either:

- Step `n - 1`
- Step `n - 2`

So:

```text
ways(n) = ways(n - 1) + ways(n - 2)
```

This is the Fibonacci recurrence relation.
