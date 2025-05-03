### ThreeSum Approach Summary

---

#### ✅ Set-Based Approach (Categorized by Sign)

- **Split the input list** into three categories:
  - `neg`: all negative numbers
  - `pos`: all positive numbers
  - `zero`: all zeroes

- **Use sets** for quick lookup:
  - `neg_set` and `pos_set` are used to check for complements in constant time.

- **Handle edge cases**:
  - If there's at least one `0`, for any `num` in `pos_set`, check if `-num` is in `neg_set` → add `(-num, 0, num)` to result.
  - If there are three or more zeroes, add the triplet `(0, 0, 0)`.

- **Check for valid triplets**:
  - For all pairs of negative numbers `(neg[i], neg[j])`, compute target `-(neg[i] + neg[j])` and check if it's in `pos_set`.
  - For all pairs of positive numbers `(pos[i], pos[j])`, compute target `-(pos[i] + pos[j])` and check if it's in `neg_set`.

- **Avoid duplicates**:
  - Store all found triplets as **sorted tuples** in a set to ensure uniqueness.

- **Return result**:
  - Convert the set of tuples into a list of lists before returning.

---

#### ✅ Two-Pointer Approach (Sorted Array)

- **Sort the input list** to enable efficient pointer movement and duplicate skipping.

- **Iterate through the list** with index `i` representing the first number of the triplet.
  - Skip duplicates for `nums[i]` to avoid repeated triplets.

- **Initialize two pointers**:
  - `left` starts at `i + 1`
  - `right` starts at the end of the list

- **Move pointers based on the sum**:
  - If `nums[i] + nums[left] + nums[right] == 0`, add the triplet to the result.
  - If the sum is **less than 0**, move `left` forward to increase the total.
  - If the sum is **greater than 0**, move `right` backward to decrease the total.

- **Skip duplicates** for `left` and `right` to prevent repeated triplets.

- **Return result**:
  - Collect all valid triplets in a list of lists.
