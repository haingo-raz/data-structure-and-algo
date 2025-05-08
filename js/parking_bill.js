/* Calculate parking fare if:
- The entrance fee of the car parking lot is 2;
- The first full or partial hour costs 3;
- Each successive full or partial hour (after the first) costs 4.
*/

E = "10:00"
L = "13:30"

function Solution(E, L) {
    function convertToMinutes(time) {
        const [hours, minutes] = time.split(":").map(Number);
        return hours * 60 + minutes;
    }

    const entranceFee = 2;
    const firstHourFee = 3;
    const additionalHourFee = 4;

    const start = convertToMinutes(E);
    const end = convertToMinutes(L);
    const duration = end - start;

    if (duration <= 60) {
        return entranceFee + firstHourFee;
    } else {
        const extraHours = Math.ceil((duration - 60) / 60); // round up partial hours
        return entranceFee + firstHourFee + (extraHours * additionalHourFee);
    }
}