"""
Regex groups using or "|"
OR is represented using |
You can define a group using ()
You can define explicit character ranges using []
"""
"""
import re 

In [2]: match_digits_and_words = ('(\d+|\w+)')
In [3]: re.findall(match_digits_and_words, 'He has 11 cats.')
"""

"""
Regex ranges and groups
pattern	matches	example
[A-Za-z]+	upper and lowercase English alphabet	'ABCDEFghijk'
[0-9]	    numbers from 0 to 9	9
[A-Za-z\-\.]+	upper and lowercase English alphabet, - and .	'My-Website.com'
(a-z)	    a, - and z	'a-z'
(\s+l,)	    spaces or a comma	', '
"""
"""
Given the following string, which of the below patterns is the best tokenizer? If possible, you want to retain sentence punctuation as separate tokens, but have '#1' remain a single token.

my_string = "SOLDIER #1: Found them? In Mercea? The coconut's tropical!"
The string is available in your workspace as my_string, and the patterns have been pre-loaded as pattern1, pattern2, pattern3, and pattern4, respectively.

Additionally, regexp_tokenize has been imported from nltk.tokenize. You can use regexp_tokenize() with my_string and one of the patterns as arguments to experiment for yourself and see which is the best tokenizer.

Instructions
50 XP
Possible Answers
r"\w+(\?!)"
.. r"(\w+|#\d|\?|!)" 
r"(#\d\w+\?!)"
r"\s+"
"""

# Import the necessary modules
from nltk.tokenize import regexp_tokenize
from nltk.tokenize import TweetTokenizer

# Define a regex pattern to find hashtags: pattern1
pattern1 = r"#\w+"

# Use the pattern on the first tweet in the tweets list
regexp_tokenize(tweets[0], pattern1)

# Write a pattern that matches both mentions and hashtags
pattern2 = r"([@#]\w+)"

# Use the pattern on the last tweet in the tweets list
regexp_tokenize(tweets[-1], pattern2)

# Use the TweetTokenizer to tokenize all tweets into one list
tknzr = TweetTokenizer()
all_tokens = [tknzr.tokenize(t) for t in tweets]
print(all_tokens)

# Tokenize and print all words in german_text
all_words = word_tokenize(german_text)
print(all_words)

# Tokenize and print only capital words
capital_words = r"[A-ZÜ]\w+"
print(regexp_tokenize(german_text, capital_words))

# Tokenize and print only emoji
emoji = "['\U0001F300-\U0001F5FF'|'\U0001F600-\U0001F64F'|'\U0001F680-\U0001F6FF'|'\u2600-\u26FF\u2700-\u27BF']"
print(regexp_tokenize(german_text, emoji))
