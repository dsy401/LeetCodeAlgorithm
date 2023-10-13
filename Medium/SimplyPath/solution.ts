// https://leetcode.com/problems/simplify-path/
const simplifyPath = (path: string): string => {
    const pathArr = path.split('/')

    const conicalPathArr: string[] = []

    for (const dir of pathArr) {
        if (dir === '.' || dir === '') continue

        if (dir == '..') {
            conicalPathArr.pop()
            continue
        }

        conicalPathArr.push(dir)
    }

    return "/" + conicalPathArr.join("/")
}


console.log("Input: '/home/' Output: '/home' Actual:", simplifyPath("/home/"))
console.log("Input: '/../' Output: '/' Actual:", simplifyPath("/../"))
console.log("Input: '/home//foo/' Output: '/home/foo' Actual:", simplifyPath("/home//foo/"))
