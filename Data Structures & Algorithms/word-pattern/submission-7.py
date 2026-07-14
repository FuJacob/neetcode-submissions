class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        word_to_letter = {}
        letter_to_word = {}
        if len(words) != len(pattern):
            return False
        for w,l in zip(words, pattern):
            if w in word_to_letter and l in letter_to_word:
                if l != word_to_letter[w] or w != letter_to_word[l]:
                    return False
            if w in word_to_letter and word_to_letter[w] != l:
                return False
            if l in letter_to_word and letter_to_word[l] != w:
                return False
            word_to_letter[w] = l
            letter_to_word[l] = w
        return True