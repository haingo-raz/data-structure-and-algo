// Return distinct values in an array

let A = [2, 1, 1, 2, 3, 1, 4, 5, 6, 0, 0, 1];

function Solution(A) {
    return new Set(A).size
}

console.log(Solution(A))