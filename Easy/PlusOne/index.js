// https://leetcode.com/problems/plus-one/
const plusOne = (digits) => {
    const reverseDigits = digits.reverse()

    let i =0
    while (i !== reverseDigits.length) {
        if (i === 0) {
            reverseDigits[i] = reverseDigits[i] + 1

            if (reverseDigits[i] >= 10) {
                reverseDigits[i] = 0
                reverseDigits[i + 1] = (reverseDigits[i + 1] ?? 0) + 1
            }
        } else {
            if (reverseDigits[i] >= 10) {
                reverseDigits[i] = 0
                reverseDigits[i + 1] = (reverseDigits[i + 1] ?? 0) + 1
            }
        }

        i ++
    }

    return reverseDigits.reverse()
};

console.log(plusOne([6]))
