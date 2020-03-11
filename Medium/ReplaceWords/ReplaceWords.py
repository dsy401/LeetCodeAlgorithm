class Solution(object):
    def replaceWords(self, dict, sentence):
        sentence_list = sentence.split(' ')
        for i in range(len(sentence_list)):
            change_word = self.first_substring(dict,sentence_list[i])
            if change_word != -1:
                sentence_list[i] = change_word


        result = ""
        for word in sentence_list:
            result = result + word + " "

        return result.strip()

    def first_substring(self,word_list, string):
        substring_list = []
        for i in range(len(string)):
            substring_list.append(string[:i + 1])

        for word in word_list:
            if word in substring_list:
                return word

        return -1


a = Solution()
print(a.replaceWords(
    ['a','b','c'],
    "aadsfasf absbs bbab cadsfafs"
))

