# Definition
Time complexity is a way to describe how long a computer program takes to run, depending on the size of the input.

---

### Common Time Complexity Notations
- **O(1)**: Constant time — The algorithm's runtime does not depend on the input size.
- **O(log n)**: Logarithmic time — The runtime grows logarithmically as input size increases.
- **O(n)**: Linear time — The runtime grows directly proportional to the input size.
- **O(n log n)**: Quasilinear time — Often found in efficient sorting algorithms (e.g., Merge Sort).
- **O(n²)**: Quadratic time — Runtime grows quadratically; often seen in nested loops.
- **O(2ⁿ)**: Exponential time — Runtime doubles with each additional input size; often impractical for large inputs.

### Example
- **Linear Search**:  
  If you search for an item in an unsorted list of `n` elements:
  - Best case: `O(1)` (item is the first element).
  - Worst case: `O(n)` (item is the last or absent).
  - Average case: `O(n)`.