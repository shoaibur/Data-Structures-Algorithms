class Solution:
    def calculate(self, s: str) -> int:
        
        prev_operator = '+'
        
        results = 0
        temp = 0
        num = 0
        
        for char in s+'+':
            if char.isdigit():
                num = num * 10 + int(char)
            elif char in '+-*/':
                curr_operator = char
                if prev_operator == '+':
                    results += temp
                    temp = num
                elif prev_operator == '-':
                    results += temp
                    temp = -num
                elif prev_operator == '*':
                    temp *= num
                else:
                    temp = int(temp / num)
                num = 0
                prev_operator = curr_operator
            else:
                pass
        return results + temp
