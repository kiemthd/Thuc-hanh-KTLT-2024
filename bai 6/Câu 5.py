class Solution:
    def reverse_words(self, s: str) -> str:
        return ' '.join(reversed(s.split()))
# Sử dụng class
solution = Solution()
print(solution.reverse_words('hello .py'))
