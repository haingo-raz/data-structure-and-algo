// Return the value of the unpaired element
// Using XOR

const A = [9, 3, 9, 3, 9, 7, 9]

function solution(A) {
    let unpaired = 0;
    for (let i = 0; i < A.length; i++) {
        unpaired ^= A[i];
    }
    return unpaired;
}

console.log(solution(A))