class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        add = 0
        num = 0
        temp = n
        while temp :
            digit = temp%10
            temp = temp/10
            if digit == 0:
                continue
            else :
                num = num*10 + digit
                add += digit
        temp = 0
        while num :
            digit = num%10
            num = num/10
            temp = temp*10 + digit
        return temp * add