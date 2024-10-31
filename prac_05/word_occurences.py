"""
Word Occurrences
Estimate: 25 minutes
Actual:   37 minutes
"""
text = input("Enter a string: ")
words = text.split(" ")
word_to_occurrence = {}
for word in words:
    if word in word_to_occurrence:
        word_to_occurrence[word] += 1
    else:
        word_to_occurrence[word] = 1
width = max([len(word) + 1 for word, words in word_to_occurrence.items()])
for word, count in sorted(word_to_occurrence.items()):
    print(f"{word:{width}}: {count}")
