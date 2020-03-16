class Solution(object):
    def sortString(self, s):
        s_list = list(s)
        s_list.sort()
        s_dict = {}
        for char in s_list:
            if char not in s_dict:
                s_dict[char] = 1
            else:
                s_dict[char] += 1

        result = ""

        while s_dict:
            for key in s_dict:
                result += key
                s_dict[key] = s_dict[key]-1
            delete = [key for key in s_dict if s_dict[key] == 0]

            # delete the key
            for key in delete: del s_dict[key]

            s_dict = self.reverse_dict(s_dict)




        return result

    def reverse_dict(self,s):
        new_list = []
        s_dict = {}
        for key in s:
            new_list+= [key]*s[key]

        new_list.reverse()
        for char in new_list:
            if char not in s_dict:
                s_dict[char] = 1
            else:
                s_dict[char] += 1

        return s_dict

a = Solution()

assert "abccbaabccba" == a.sortString("aaaabbbbcccc")
assert "art" == a.sortString('rat')