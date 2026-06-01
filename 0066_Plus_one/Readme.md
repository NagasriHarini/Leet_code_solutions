# Plus One (LeetCode 66)

## Problem Statement

You are given a large integer represented as an integer array `digits`, where each `digits[i]` is the ith digit of the integer.

The digits are ordered from most significant to least significant in left-to-right order.

The large integer does not contain any leading zeros.

Increment the large integer by one and return the resulting array of digits.

---

## Example 1

**Input**

```text
digits = [1,2,3]
```

**Output**

```text
[1,2,4]
```

**Explanation**

```text
The array represents the integer 123.
Incrementing by one gives 124.
```

---

## Example 2

**Input**

```text
digits = [4,3,2,1]
```

**Output**

```text
[4,3,2,2]
```

**Explanation**

```text
The array represents the integer 4321.
Incrementing by one gives 4322.
```

---

## Example 3

**Input**

```text
digits = [9]
```

**Output**

```text
[1,0]
```

**Explanation**

```text
The array represents the integer 9.
Incrementing by one gives 10.
```

---

## Constraints

```text
1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading zeros
```
