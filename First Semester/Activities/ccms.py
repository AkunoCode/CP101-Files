for i in range(2):
    string = input("Please enter a string: ").split()

    word_counts = {}

    for words in string:
        if words in word_counts.keys():
            continue
        else:
            word_counts[words] = string.count(words)

    print("Here are the word counts:")
    print(*[f"{word} - {count}" for word, count in word_counts.items], sep=",")