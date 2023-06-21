from collections import deque


class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        list_s = list(s)
        word = ''
        for c in list_s:
            if c == ' ':
                if len(word) > 0:
                    stack.append(word)
                    word = ''
            else:
                word += c
        if len(word) > 0:
            stack.append(word)

        return " ".join(reversed(stack))

    # Split + Reverse
    def reverseWords2(self, s: str) -> str:
        return " ".join(reversed(s.split()))

    # Dequeue
    def reverseWords3(self, s: str) -> str:
        left, right = 0, len(s) - 1
        while left <= right and s[left] == ' ':
            left += 1
        while left <= right and s[right] == ' ':
            right -= 1

        d, word = deque(), ''
        while left <= right:
            if s[left] == ' ' and word:
                d.appendleft(word)
                word = ''
            elif s[left] != ' ':
                word += s[left]
            left += 1
        d.appendleft(word)

        return ' '.join(d)


sol = Solution()
res = sol.reverseWords("a good   example")
print(res)
