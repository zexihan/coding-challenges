"""
brute force
"""
class Solution_1:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        if not sentence:
            return rows * cols
        row, col, idx, cnt = 1, cols, 0, 0
        total_len = 0
        for i in range(len(sentence)):
            total_len += len(sentence[i]) + 1
        while row <= rows:
            if col >= total_len:
                cnt += col // total_len
                col = col % total_len
            if col >= len(sentence[idx]):
                col -= len(sentence[idx])
                if col > 0:
                    col -= 1
                idx += 1
                if idx == len(sentence):
                    cnt += 1
                    idx = 0
            else:
                row += 1
                col = cols
        return cnt

"""
much faster
reformatted sentence: ["ab", "cde", "f"] -> "ab cde f"
count: how many characters of the reformatted sentence is on the screen
count % length of reformatted sentence: the starting position of the next row
Answer: count / length of reformatted sentence
"""
class Solution_2:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        s = " ".join(sentence) + " "
        count = 0
        for i in range(rows):
            count += cols
            if s[count % len(s)] == " ":
                count += 1
            else:
                while count > 0 and s[(count - 1) % len(s)] != ' ':
                    count -= 1
        return count // len(s)
