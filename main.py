def palindrome(word):
    if len(word) == 0:
        return False
    elif word == word[::-1]:
        return True
    else:
            return False
    
word = input("Give me a word: ")
word = word.lower()
word = word.replace(" ","")
word = word.strip()

answer = palindrome(word)
print(answer)