// https://leetcode.com/problems/sort-colors/
function sortColors(nums: number[]): void {
    nums.sort((a,b) => a - b)
}


const nums1 =[2,0,2,1,1,0]
sortColors(nums1)
console.log(nums1)

const nums2 = [2,0,1]
sortColors(nums2)
console.log(nums2)
