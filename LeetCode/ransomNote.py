from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Count the frequency of each character in ransomNote and magazine
        ransomCount = Counter(ransomNote)
        magazineCount = Counter(magazine)

        # Check if for every character in ransomNote, magazine has enough characters
        for char, count in ransomCount.items():
            if count > magazineCount[char]:
                return False

        return True

    def canConstructNoCounter(self, ransomNote: str, magazine: str) -> bool:
        hash1 = {}
        hash2 = {}

        for c in ransomNote:
            if hash1.get(c) is None:
                hash1[c] = 0
            hash1[c] += 1


        for c in magazine:
            if hash2.get(c) is None:
                hash2[c] = 0
            hash2[c] += 1

        for c in hash1:
            if hash1[c] > hash2.get(c, 0): # If ransomNote needs more of C than magazine has
                return False

        return True
if __name__ == "__main__":
    solution = Solution()
    print(solution.canConstructNoCounter(ransomNote="a", magazine="b"))