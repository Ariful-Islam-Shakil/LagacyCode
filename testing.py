# utils.py

import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from StringIO import StringIO  # Python 2 only

def fetch_website_title(url):
    """Get website title using requests + BeautifulSoup."""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.title.string if soup.title else 'No Title Found'

def calculate_mean(arr):
    """Calculate mean using numpy."""
    return np.mean(arr)

def create_dataframe():
    """Create pandas DataFrame and check if 'score' column exists."""
    data = {'name': ['Alice', 'Bob', 'Charlie'], 'score': [85, 90, 95]}
    df = pd.DataFrame(data)
    if 'score' in df.columns:
        return df
    return pd.DataFrame()


def count_words(text):
    """Count word frequency using collections.Counter."""
    words = text.lower().split()
    return Counter(words)

def say_hello(name):
    """Old-style string formatting for greeting."""
    return "Hello, %s!" % name

def generate_range(n):
    """Generate squares using xrange (Python 2 only)."""
    result = []
    for i in xrange(n):
        result.append(i * i)
    return result

def string_io_example():
    """StringIO example for string buffer (Python 2 only)."""
    buffer = StringIO()
    buffer.write("This is a string buffer.\n")
    buffer.write("Works in Python 2.7 with StringIO module.\n")
    content = buffer.getvalue()
    buffer.close()
    return content

def dictionary_iteration():
    """Iterate dictionary with iteritems() (Python 2 only)."""
    d = {'a': 1, 'b': 2}
    result = []
    for k, v in d.iteritems():
        result.append("%s => %d" % (k, v))
    return result

def exception_handling_demo():
    """Python 2 style exception handling."""
    try:
        return 10 / 0
    except ZeroDivisionError, e:
        return "Caught an error: %s" % str(e)

# main.py

def main():
    print say_hello("Python 2.7 User")

    title = fetch_website_title("https://www.example.com")
    print "Website Title:", title

    mean_val = calculate_mean([5, 15, 25])
    print "Mean Value:", mean_val

    df = create_dataframe()
    print "DataFrame:\n", df

    # result = utils.plot_scores()
    # print result

    text = "Python is fun and Python is powerful"
    word_count = count_words(text)
    print "Word Counts:"
    for word, count in word_count.iteritems():  # Python 2 style dictionary iteration
        print "%s: %d" % (word, count)

    print "Generated Range Squares:", generate_range(5)

    print "StringIO Buffer Output:\n" + string_io_example()

    print "Dictionary Iteration Output:"
    for line in dictionary_iteration():
        print line

    print "Exception Handling Test:", exception_handling_demo()

if __name__ == '__main__':
    main()
