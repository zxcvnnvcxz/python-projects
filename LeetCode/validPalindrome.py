def isPalindrome(s: str) -> bool:
    s = ''.join(filter(str.isalnum, s))
    s = s.lower()
    return s == s[::-1]

if __name__ == "__main__":
    string = "A man, a plan, a canal: Panama"
    string1 = "race a car"
    string2 = "0P"
    print(isPalindrome(string))