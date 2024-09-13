class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:

        # XOR 运算 a ^ a = 0  a ^ 0 = a

        # Step 1: Create a prefix XOR array
        prexor = [0]
        for n in arr:
            prexor.append(prexor[-1] ^ n)

        # Step 2: Process each query and find the XOR for the subarray
        res = []
        for left, right in queries:
            res.append(prexor[left] ^ prexor[right+1])
        return res

        """超时方案
        res = []
        n = len(queries)
        for i in range(n):
            left = queries[i][0]
            right = queries[i][1]
            tmp = 0
            for j in range(left, right+1):
                tmp ^= arr[j]
            res.append(tmp)
        
        return res
        """
