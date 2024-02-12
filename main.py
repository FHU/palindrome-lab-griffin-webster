def palindrome(word):
    if len(word) == 0:
        return False
    else:
        for i in word:
            if word == word[::-1]:
                continue
            else:
                return False
        return True 
    
word = input()
word = word.lower()
word = word.replace(" ","")
word = word.strip()

palindrome(word)
