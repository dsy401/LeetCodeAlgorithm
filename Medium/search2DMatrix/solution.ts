// https://leetcode.com/problems/search-a-2d-matrix
function searchMatrix(matrix: number[][], target: number): boolean {
    for (let i = 0; i < matrix.length; i++) {

        if (i === matrix.length - 1 || (target > matrix[i][0] && target < matrix[i+1][0])) {
            for (let j =0; j< matrix[i].length; j ++) {
                if (matrix[i][j] === target) return true
            }
            continue
        }

        if (target === matrix[i][0] || target === matrix[i+1][0]) return true
    }

    return false
}


console.log(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
console.log(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))
