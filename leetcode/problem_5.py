class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        longest = None
        for i1 in range(len(s)):
            for i2 in range(i1 + len(longest) if longest else 0, len(s)):
                ss = s[i1 : i2 + 1]
                if ss == ss[::-1]:
                    if longest is None:
                        longest = ss
                    if len(ss) > len(longest):
                        longest = ss
        return longest


def main():
    print(Solution().longestPalindrome("babad"))
    print(Solution().longestPalindrome("a"))
    print(Solution().longestPalindrome("aaaaaaa"))
    print(Solution().longestPalindrome("bb"))


if __name__ == "__main__":
    main()
