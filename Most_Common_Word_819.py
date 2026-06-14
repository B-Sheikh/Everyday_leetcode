class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        t = ""
        for i in paragraph:
            if i in "!?',;.":
                t = t + " "
            else:
                t = t + i
        dic = {}
        for i in t.split():
            i = i.lower()
            if i not in banned:
                if i not in dic:
                    dic[i] = 1
                else:
                    dic[i] = dic[i] + 1
        m = max(dic.values())
        for j in dic:
            if dic[j] == m:
                return j
