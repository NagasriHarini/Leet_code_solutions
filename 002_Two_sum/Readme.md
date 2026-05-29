# Add Two Numbers (LeetCode 2)

## Problem Statement

You are given two non-empty linked lists representing two non-negative integers.

- The digits are stored in **reverse order**.
- Each node contains a single digit.
- Add the two numbers and return the sum as a linked list.
- The two numbers do not contain leading zeros, except the number `0` itself.

---

## Example 1

**Input**

```text
l1 = [2,4,3]
l2 = [5,6,4]
```

**Output**

```text
[7,0,8]
```

**Explanation**

```text
342 + 465 = 807
```

Since the digits are stored in reverse order:

```text
[2,4,3] -> 342
[5,6,4] -> 465
```

Result:

```text
807 -> [7,0,8]
```

---

## Example 2

**Input**

```text
l1 = [0]
l2 = [0]
```

**Output**

```text
[0]
```

---

## Example 3

**Input**

```text
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
```

**Output**

```text
[8,9,9,9,0,0,0,1]
```

---

## Constraints

- Number of nodes in each linked list: `1 <= n <= 100`
- `0 <= Node.val <= 9`
- No leading zeros except for the number `0` itself.

---

## Key Observation

Since digits are stored in reverse order, we can add them exactly like elementary-school addition:

1. Add corresponding digits.
2. Keep track of the carry.
3. Create a new node for each digit of the result.
4. Continue until both lists and the carry are exhausted.

---

## Time Complexity

```text
O(max(n, m))
```

where:

- `n` = length of `l1`
- `m` = length of `l2`

## Space Complexity

```text
O(max(n, m))
```

for the output linked list.
