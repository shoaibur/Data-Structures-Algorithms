class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        suggestions = []
        prefix = ''
        for char in searchWord:
            temp = []
            prefix += char
            # print(prefix)
            for word in products:
                if len(temp) == 3:
                    break
                if word.startswith(prefix):
                    temp.append(word)
            suggestions.append(temp)
        return suggestions
