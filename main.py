#REMOVE PASS AND FIX THIS FUNCTION
def palindrome(word):
    if word == word[::-1]:
        return True
    elif word == "":
        return False
    else:
        return False
    
word = input()
word = word.lower()
word = word.strip()
word = word.replace(" ","")

answer = palindrome(word)

print(answer)
