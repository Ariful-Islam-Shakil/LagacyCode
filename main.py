# main.py

import utils

def main():
    print utils.say_hello("Python 2.7 User")

    title = utils.fetch_website_title("https://www.example.com")
    print "Website Title:", title

    mean_val = utils.calculate_mean([5, 15, 25])
    print "Mean Value:", mean_val

    df = utils.create_dataframe()
    print "DataFrame:\n", df

    # result = utils.plot_scores()
    # print result

    text = "Python is fun and Python is powerful"
    word_count = utils.count_words(text)
    print "Word Counts:"
    for word, count in word_count.iteritems():  # Python 2 style dictionary iteration
        print "%s: %d" % (word, count)

    print "Generated Range Squares:", utils.generate_range(5)

    print "StringIO Buffer Output:\n" + utils.string_io_example()

    print "Dictionary Iteration Output:"
    for line in utils.dictionary_iteration():
        print line

    print "Exception Handling Test:", utils.exception_handling_demo()

if __name__ == '__main__':
    main()
