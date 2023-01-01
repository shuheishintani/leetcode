class Solution:
    # reverse
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for c in s:
            if c.isalnum():
                new_str += c.lower()
        return new_str == new_str[::-1]

    # reverse (using lambda)
    def isPalindrome2(self, s: str) -> bool:
        filtered_chars = filter(lambda ch: ch.isalnum(), s)
        lowercase_filtered_chars = map(lambda ch: ch.lower(), filtered_chars)
        original_list = list(lowercase_filtered_chars)
        reversed_list = original_list[::-1]
        return original_list == reversed_list

    # two pointers
    def isPalindrome3(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    # implementation of isalnum()
    def alphanum(self, c):
        return ord("A") <= ord(c) <= ord("Z") \
            or ord("a") <= ord(c) <= ord("z") \
            or ord("0") <= ord(c) <= ord("9")
