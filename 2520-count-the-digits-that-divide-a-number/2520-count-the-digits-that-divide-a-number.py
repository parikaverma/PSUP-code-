class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        a=0
        b=str(num)
        for i in range(0,len(b)):
            if num % int(b[i]) == 0:
                a+=1
        return a