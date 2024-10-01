class Solution:
    def hammingWeight(self, n: int) -> int:

        # method 1
        # n&(n-1) will change the righmost "1" bit to "0" bit
        # so we can count the "1" bit by repeating the iteration until n becomes 0

        res = 0
        while n:
            n &= n-1
            res += 1

        return res

        '''
        # method 2
        # if n & 1 = 1 then the last bit of n is 1, then right shift n

        res = 0
        while n:
            res += n & 1
            n >>= 1
        return res

        # method 3
        return bin(n).count('1')
        

        # method 4
        # > python 3.10
        return n.bit_count()
        '''
