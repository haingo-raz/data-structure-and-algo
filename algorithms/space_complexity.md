# Definition
Space complexity measures how much memory a program needs to run based on the input size.

Space complexity measures the amount of memory an algorithm uses, including:
1. Input size.
2. Temporary variables.
3. Recursion stack space (if any).

---

### Components of Space Complexity
1. **Fixed Part**:  
   Memory used regardless of input size (e.g., constants, instructions).
   
2. **Variable Part**:  
   Memory used by variables, structures, and recursion, which depends on the input size.

### Common Space Complexity Notations
- **O(1)**: Constant space — The memory usage does not depend on the input size.
- **O(n)**: Linear space — Memory usage grows proportionally to the input size.
- **O(n²)**: Quadratic space — Memory grows quadratically with the input size.

### Example
- **Merge Sort**:
  - Space complexity: `O(n)` (for temporary arrays used during merging).
  
- **Bubble Sort**:
  - Space complexity: `O(1)` (no extra memory apart from a few variables).

---