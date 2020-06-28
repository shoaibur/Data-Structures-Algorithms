def mostCommonWord(paragraph)
    banned = set(banned)
    for punctuation in "!?',;.":
        paragraph = paragraph.replace(punctuation, ' ')
    words = paragraph.lower().split()
    d = {}
    for word in words:
        if word not in banned:
            d[word] = d.get(word, 0) + 1
    return [word for word, count in d.items() if max(d.values())==count][0]
