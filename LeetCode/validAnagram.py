def isAnagram(s:str, t:str) -> bool:
    temp = []
    temp1 = []
    for c in s:
        temp.append(c)
    temp.sort()

    for c in t:
        temp1.append(c)
    temp1.sort()

    if temp == temp1:
        return True
    else:
        return False


def isAnagram1(s: str, t: str) -> bool:
    # Step 1: Early check on lengths
    if len(s) != len(t):
        return False

    # Step 2: Create a character count dictionary
    char_count = {}

    # Count characters in the first string
    for c in s:
        char_count[c] = char_count.get(c, 0) + 1

    # Decrease counts based on the second string
    for c in t:
        if c in char_count:
            char_count[c] -= 1
            # If count goes below zero, not an anagram
            if char_count[c] < 0:
                return False
        else:
            # Character not found in the first string
            return False

    # Step 3: All counts should be zero
    return all(count == 0 for count in char_count.values())


from collections import Counter


def isAnagram2(s:str, t:str) -> bool:
    return Counter(s) == Counter(t)


if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    print(isAnagram2(s,t))