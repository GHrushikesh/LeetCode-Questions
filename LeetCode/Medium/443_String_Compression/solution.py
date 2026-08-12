class Solution:
    def compress(self, chars: List[str]) -> int:
        read = 0
        write = 0
        while read < len(chars):
            current = chars[read]
            count = 0
            while read < len(chars) and chars[read] == current:
                count += 1
                read += 1
            chars[write] = current
            write += 1
            if count > 1:
                count_str = str(count)
                for ch in count_str:
                    chars[write] = ch
                    write += 1
        return write