# Intuition Behind `firstMissingPositive` Algorithm

## Goal
- Find the **smallest missing positive integer** from an unsorted array of integers.

---

## Key Concepts

- We only care about **positive integers** starting from 1.
- The index positions in the array can be used to **track presence** of numbers.
- We can **mark existing numbers** by converting values at certain indices to negative.

---

## Step-by-Step Intuition

### 1. **Ignore Irrelevant Numbers**
- Filter out all non-positive numbers.
- Why? They can't be the smallest missing positive.

### 2. **Mark Existing Numbers via Indices**
- Treat index `i` as representing the number `i + 1`.
- For each number `n`, if `n` is in the range `1` to `nums.length`, mark its corresponding index (`n - 1`) negative.
- Why? A negative value at index `i` indicates the number `i + 1` is present.

### 3. **Identify the Missing Number**
- The first index `i` with a positive value implies number `i + 1` was never marked (i.e., missing).
- Return `i + 1`.

### 4. **All Numbers Are Present**
- If all indices are negative (all numbers `1` through `nums.length` exist), then the smallest missing positive is `nums.length + 1`.

---

## Time and Space Complexity

- **Time Complexity:** `O(n)` — Three linear passes through the array.
- **Space Complexity:** `O(1)` extra — Works in-place with no additional data structures.

---

## Core Insight

- This algorithm **reuses the input array as a hash map** using index-based marking.
- It avoids extra space by encoding presence information directly into the array using signs.
