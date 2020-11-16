"""
    A palindrome is a word that reads the same forward and backward.
    Using recursion:
    "tot"

    Pseudo code:
        1. Compare first and last letter: t == t
        2. Create sub array without the 1st and last letter
        3. Repeat 1 - 2 until sub array length is 0. If all are true then, word is Palindrome

"""

def isPalindrome(w):
    if len(w) > 0:
        if w[0] == w[-1]:
            isPalindrome(w[-(len(w)-1):-2])
        else:
            return False
    return True





if __name__ == "__main__":
    print(isPalindrome(["t"])) # true
    print(isPalindrome(["t", "o"])) # false
    print(isPalindrome(["t", "o", "t"])) # true
    print(isPalindrome("rotor")) # true
    print(isPalindrome("rt")) # false
    print(isPalindrome("r")) # true