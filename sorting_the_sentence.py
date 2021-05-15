class Solution:
    def sortSentence(self, sentence: str) -> str:
        words = sentence.split()
        sorted_words = ['' for _ in words]
        for word_index in words:
            word, index = word_index[:-1], int(word_index[-1])
            sorted_words[index-1] = word
        
        return ' '.join(sorted_words)


tests = [
    (
        ("is2 sentence4 This1 a3",),
        "This is a sentence",
    ),
    (
        ("Myself2 Me1 I4 and3",),
        "Me Myself and I",
    ),
]