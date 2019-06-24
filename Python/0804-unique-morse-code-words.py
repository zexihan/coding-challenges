class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        table = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                 "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        uniqM = set()
        for w in words:
            uniqM.add(''.join([table[ord(c) - ord('a')] for c in w]))
        return len(uniqM)