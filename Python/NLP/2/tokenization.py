"""
Turning a string or document into tokens (smaller chunks)
One step in preparing a text for NLP
Many different theories and rules
You can create your own rules using regular expressions
Some examples:
Breaking out words or sentences
Separating punctuation
Separating all hashtags in a tweet
"""

"""
nltk library
nltk: natural language toolkit

Other nltk tokenizers
sent_tokenize: tokenize a document into sentences
regexp_tokenize: tokenize a string or document based on a regular expression pattern
TweetTokenizer: special class just for tweet tokenization, allowing you to separate hashtags, mentions and lots of exclamation points!!!
"""
"""
from nltk.tokenize import word_tokenize
word_tokenize("Hi there!") 
"""
"""
Why tokenize?
Easier to map part of speech
Matching common words
Removing unwanted tokens
"""
# Import necessary modules
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

# Split scene_one into sentences: sentences
sentences = sent_tokenize(scene_one)

# Use word_tokenize to tokenize the fourth sentence: tokenized_sent
tokenized_sent = word_tokenize(sentences[3])

# Make a set of unique tokens in the entire scene: unique_tokens
unique_tokens = set(word_tokenize(scene_one))

# Print the unique tokens result
print(unique_tokens)

# Search for the first occurrence of "coconuts" in scene_one: match
match = re.search("coconuts", scene_one)

# Print the start and end indexes of match
print(match.start(),match.end())

# Write a regular expression to search for anything in square brackets: pattern1
pattern1 = r"\[.*\]"

# Use re.search to find the first text in square brackets
print(re.search(pattern1,scene_one))

# Find the script notation at the beginning of the fourth sentence and print it
pattern2 = r"[\w\s]+:"
print(re.match(pattern2,sentences[3]))