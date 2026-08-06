# Reverse Integer (LeetCode 7)

## Problem Statement

Given a signed 32-bit integer `x`, return `x` with its digits reversed.

If reversing `x` causes the value to go outside the signed 32-bit integer range:

```text
[-2^31, 2^31 - 1]
```

then return `0`.

**Note:** You may not use 64-bit integers (signed or unsigned).

---

## Example 1

### Input

```text
x = 123
```

### Output

```text
321
```

---

## Example 2

### Input

```text
x = -123
```

### Output

```text
-321
```

---

## Example 3

### Input

```text
x = 120
```

### Output

```text
21
```

---

## Constraints

```text
-2^31 <= x <= 2^31 - 1
```

or

```text
-2147483648 <= x <= 2147483647
```

---

## Key Observations

1. Extract the last digit using:

```python
digit = x % 10
```

2. Remove the last digit using:

```python
x //= 10
```

3. Build the reversed number:

```python
reverse = reverse * 10 + digit
```

4. Before adding a digit, check for overflow.

---

## Overflow Range

A signed 32-bit integer can store:

```text
Minimum = -2147483648
Maximum = 2147483647
```

If the reversed number exceeds this range, return:

```text
0
```

---

## Approach

1. Store the sign.
2. Work with the absolute value.
3. Repeatedly extract digits.
4. Construct the reversed number.
5. Restore the sign.
6. Check for 32-bit overflow.

---

## Time Complexity

```text
O(log10(n))
```

The number of iterations equals the number of digits.

---

## Space Complexity

```text
O(1)
```

Only a few variables are used.

---

## Example Walkthrough

### Input

```text
x = 123
```

| Step | Digit | Reverse |
|------|--------|----------|
| 1 | 3 | 3 |
| 2 | 2 | 32 |
| 3 | 1 | 321 |

Output:

```text
321
```
