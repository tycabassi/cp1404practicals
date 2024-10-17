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
max_length = max([len(word) + 1 for word, words in word_to_occurrence.items()])  # +1 as it looks crammed with no space
for word, count in sorted(word_to_occurrence.items()):
    print(f"{word:{max_length}}: {count}")
