"""
Word Occurrences
Estimate: 25 minutes
Actual:    minutes
"""
text = input("Enter a string: ")
words = text.split(" ")
word_to_occurrence = {}
for word in words:
    if word in word_to_occurrence:
        word_to_occurrence[word] += 1
    else:
        word_to_occurrence[word] = 1
for word, count in word_to_occurrence.items():
    print(f"{word}: {count}")

