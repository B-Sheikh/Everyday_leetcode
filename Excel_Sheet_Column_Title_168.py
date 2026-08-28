class Solution(object):
    def convertToTitle(self, columnNumber):
        t = ""
        while columnNumber > 0:
            columnNumber  = columnNumber -1
            t = t + chr(columnNumber%26+ord("A"))
            columnNumber = columnNumber//26
        return t[::-1]
        
