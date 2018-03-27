user_sentence = input("Text: ")
split_words = user_sentence.split(" ")
split_words.sort()
longest_word = max(split_words)
max_space = 0
word_collection = {}
for word in split_words:
    if word in word_collection:
        word_collection[word] += 1
    else:
        word_collection[word] = 1
for letter in longest_word:
    max_space += 1
for word in word_collection:
    print("{:{}} = {}".format(word, max_space, word_collection[word]))

print("Finished")
