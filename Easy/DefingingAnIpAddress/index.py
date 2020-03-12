class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """

        address_list = list(address)
        result = ""
        for word in address_list:
            if word == ".":
                result += "[.]"
            else:
                result+=word

        return result





a = Solution()
print(a.defangIPaddr("1.1.1.1"))