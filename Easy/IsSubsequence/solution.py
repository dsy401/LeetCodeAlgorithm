def isSubsequence(self, s: str, t: str) -> bool:
    length = len(s)
    if length == 0:
        return True
    count = 0
    for i in t:
        if i == s[count]:
            count += 1
        if count >= length:
            return True
    if count < length:
        return False
    return True