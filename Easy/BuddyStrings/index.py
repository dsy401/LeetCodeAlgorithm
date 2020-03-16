class Solution(object):
    def buddyStrings(self, A, B):
        # if len(A) != len(B): return False
        #
        # for i in range(len(A)):
        #     for j in range(len(A)):
        #         if i != j:
        #             if self.swap(A, i, j) == B:
        #                 return True

        return self.swap(A,0,1)


    def swap(self,string,pos1,pos2):
        sub_string1 = string[:pos1]
        sub_string2 = string[pos2+1:]
        mid_string = string[pos1+1:pos2]
        return sub_string1 + string[pos2] + mid_string + string[pos1]+sub_string2

a = Solution()

print(a.buddyStrings("ab","ab"))