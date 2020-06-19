    def longestDupSubstring(self, S: str) -> str:
        n = len(S)
        d = set()
        maxlen = 0
        longsubstr = ''
        for i in range(n-1):
            for j in range(i+maxlen, n):
                substr = S[i:j+1]
                if substr in d:
                    if len(substr) > maxlen:
                        maxlen = len(substr)
                        longsubstr = substr
                else:
                    d.add(substr)
        return longsubstr
