### Intuition Behind the Binary Search Solution for "Find Peak Element"

- We use binary search to efficiently find a peak in O(log n) time.
- At each step, we compare `nums[mid]` with its right neighbor `nums[mid + 1]`.

#### Case 1: `nums[mid] < nums[mid + 1]`
- We're on an increasing slope.
- A peak must exist on the right side.
- So, move the search window right: `left = mid + 1`

#### Case 2: `nums[mid] > nums[mid + 1]`
- We're on a decreasing slope.
- A peak must be on the left, possibly at `mid` itself.
- So, move the search window left: `right = mid`

- The loop continues until `left === right`, at which point we've found a peak.

#### Final Step:
- Return `left` (or `right`, since they are equal).
- This index is guaranteed to be a peak element.

This approach works even if the array is unsorted, because the direction of the slope guarantees the presence of a peak.
