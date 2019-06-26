"""
Getting started with matplotlib
Charting library used by many open source Python projects
Straightforward functionality with lots of options
Histograms
Bar charts
Line charts
Scatter plots
... and also advanced functionality like 3D graphs and animations!
"""
from matplotlib import pyplot as plt

plt.hist([1, 5, 5, 7, 7, 7, 9])
plt.show()

#Combining NLP data extraction with plotting
from matplotlib import pyplot as plt
from nltk.tokenize import word_tokenize

words = word_tokenize("This is a pretty cool tool!")
word_lengths=[len(w) for w in words]
plt.hist(word_lengths)
plt.show()

# Split the script into lines: lines
lines =holy_grail.split('\n')

# Replace all script lines for speaker
pattern = "[A-Z]{2,}(\s)?(#\d)?([A-Z]{2,})?:"
lines = [re.sub(pattern, '', l) for l in lines]

# Tokenize each line: tokenized_lines
tokenized_lines = [regexp_tokenize(s,"\w+") for s in lines]

# Make a frequency list of lengths: line_num_words
line_num_words = [len(t_line) for t_line in tokenized_lines]

# Plot a histogram of the line lengths
plt.hist(line_num_words)
# Show the plot
plt.show()