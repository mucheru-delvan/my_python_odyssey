print("🔔A simple word counter🔔\n")

def word_counter(sentence):

    words_counted = sentence.split()
    return ",".join(words_counted),len(words_counted)

while True:
    text = input("Enter a sentence: ")
    if text:
        break
    print("Please enter a sentence!")

words,total_words = word_counter(text)

print(f"\nThe words are '{words}' and they are {total_words} in number")