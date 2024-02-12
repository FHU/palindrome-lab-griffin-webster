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

# I genuinely don't know how to fix this lab. As best as I can tell, my function is returning all of expected answers. 
# No matter how many times I push it, though, it never passes any checks.