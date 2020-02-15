print("What word would you like to measure?")
word = input()

def count_words(word):
    count = 0
    for i in word:
        print(i)
        count = count + 1
    return count


# Why doesn't this work?
len = count_words(word)
print(f"The word count for {word} is: {len}")

    
