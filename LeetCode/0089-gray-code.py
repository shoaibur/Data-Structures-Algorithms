    def grayCode(self, n: int) -> List[int]:
        # Total number of codes = 2^n = 1 << n
        # ith gray code = i xor floor(i/2) = i ^ i >> 1
        out = []
        for i in range(1 << n):
            out.append( i ^ (i >> 1) )
        return out
