class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        cnt=0
        ans=set(sorted(word))
        for i in ans:
            if(i.upper() in ans and i.lower() in ans):
                cnt+=1
        return int(cnt/2)
        