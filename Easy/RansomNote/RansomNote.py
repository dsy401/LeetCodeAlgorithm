class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        if ransomNote == "":
            return True
        ransom_position = magazine.find(ransomNote)
        if ransom_position == -1:
            return False
        else:
            new_magazine = magazine[:ransom_position] + magazine[ransom_position+len(ransomNote):]

            new_ransom_position = new_magazine.find(ransomNote)

            if new_ransom_position == -1:
                return True
            else:
                return False


a = Solution()
print(a.canConstruct('aa','ab'))