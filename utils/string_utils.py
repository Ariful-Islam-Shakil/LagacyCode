from collections import Counter
from StringIO import StringIO  # Python 2 only

def say_hello(name):
    return "Hello, %s!" % name

def count_words(text):
    words = text.lower().split()
    return Counter(words)

def string_io_example():
    buffer = StringIO()
    buffer.write("This is a string buffer.\n")
    buffer.write("Works in Python 2.7 with StringIO module.\n")
    content = buffer.getvalue()
    buffer.close()
    return content

def dictionary_iteration():
    d = {'a': 1, 'b': 2}
    result = []
    for k, v in d.iteritems():
        result.append("%s => %d" % (k, v))
    return result
