import re

# Build the dictionary of words with their corresponding values.
list_words = {
    "with" : 4,
    "omg" : 7,
    "happy" : 10,
    "great" : 10,
    "awesome" : 8,
    "sad": 1,
    "disapointing"  : 2,
    "hello": 2,
    "relieved" : 9,
    "damn" : 3,
    "hard" : 4
}

# Input the tweet
tweet = input("Input the tweet:\n").lower().split()

# Clean the tweet (remove the symbols)
cleaned_tweet = [re.sub("[^a-zA-Z]", "", s) for s in tweet]

# Get the words present in the dictionary
tweet = [i for i in cleaned_tweet if i in list_words.keys()]

# Get the values of the word
vals = [list_words[i] for i in tweet]

# Computation
mood = sum(vals)/len(vals)
print(f"\nmood score is {round(mood,2)}")
if mood < 5:
    print("The tweet is sad")
else:
    print("The tweet is happy")
