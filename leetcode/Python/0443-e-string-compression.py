class Solution:
    def compress(self, chars: List[str]) -> int:
        anchor = write = 0
        for read in range(len(chars)):
            if read == len(chars) - 1 or chars[read] != chars[read + 1]:
                chars[write] = chars[anchor]
                write += 1
                if read > anchor:
                    for digit in str(read - anchor + 1):
                        chars[write] = digit
                        write += 1
                anchor = read + 1
        return write