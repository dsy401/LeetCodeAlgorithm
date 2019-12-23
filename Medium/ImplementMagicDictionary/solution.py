class MagicDictionary(object):

    def __init__(self):
        self.dict = []

    def buildDict(self, dict):
        self.dict = dict


    def search(self, word):
        for i in range(len(self.dict)):
            if is_exact_one_in_dict(word,self.dict[i]): return True
        return False

def is_exact_one_in_dict(word,compare_word):
    if word == compare_word or len(word)!=len(compare_word): return False
    count = 0
    for i in range(len(word)):
        if word[i] != compare_word[i]:
            count+=1
    return count==1

# Your MagicDictionary object will be instantiated and called as such:


