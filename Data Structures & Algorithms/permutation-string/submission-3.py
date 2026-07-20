class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        length = len(s1)

        for i in range(len(s2) - length + 1):
            subStr = sorted(s2[i:i + length])
            if subStr == s1:
                return True

        return False