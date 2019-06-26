"""
topic identification
text classification

chat bots
translations
sentiment analysis

Regular expressions
Allow us to match patterns in other strings
Find all web links in a document
Parse email addresses, remove/replace unwanted characters

"""
"""
import re

re.match('abc','abcdef')  #match(pattern, string)

word_regex='\w+'
re.match(word_regex,'hi there!')    #\w+ matches word
"""

"""
\w+	    word	    'Magic'
\d	    digit	    9
\s	    space	    ' '
.*	    wildcard	'username74'   #matches any character
+ or *	greedy match	'aaaaaa'        #matches repetative patterns
\S	    not space	'no_spaces'
[a-z]	lowercase group	'abcdefg'
"""

"""
re module
split: split a string on regex
findall: find all patterns in a string
search: search for a pattern

match: match an entire string or substring based on a pattern
Pattern first, and the string second        #for matching
May return an iterator, string, or match object
"""

# Import the regex module
import re
my_string = "akash,skajdkssjd. skjdskjdl djskfsdjk?jklkjada !"
# Write a pattern to match sentence endings: sentence_endings
sentence_endings = r"[.?!]"

# Split my_string on sentence endings and print the result
print(re.split(sentence_endings,my_string))

# Find all capitalized words in my_string and print the result
capitalized_words = r"[A-Z]\w+"
print(re.findall(capitalized_words, my_string))

# Split my_string on spaces and print the result
spaces = r"\s+"
print(re.split(spaces, my_string))

# Find all digits in my_string and print the result
digits = r"\d+"
print(re.findall(digits, my_string))