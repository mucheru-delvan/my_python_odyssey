def is_palindrome(phrase):

    phrase_cleaned = phrase.strip().lower()
    return phrase_cleaned == phrase_cleaned[::-1]

while True:
    word = input("Enter a word or phrase to check if is palindrome: ")
    if word:
        break
    print("Please enter a word or a phrase!")
    
print(is_palindrome(word))