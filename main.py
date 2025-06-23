import utils.string_utils as string_utils
import utils.math_utils as math_utils


def main():
    print string_utils.say_hello("Python 2.7 User")

    title = math_utils.fetch_website_title("https://www.example.com")
    print "Website Title:", title

    mean_val = math_utils.calculate_mean([5, 15, 25])
    print "Mean Value:", mean_val

    df = math_utils.create_dataframe()
    print "DataFrame:\n", df

    text = "Python is fun and Python is powerful"
    word_count = string_utils.count_words(text)
    print "Word Counts:"
    for word, count in word_count.iteritems():
        print "%s: %d" % (word, count)

    print "Generated Range Squares:", math_utils.generate_range(5)

    print "StringIO Buffer Output:\n" + string_utils.string_io_example()

    print "Dictionary Iteration Output:"
    for line in string_utils.dictionary_iteration():
        print line

    print "Exception Handling Test:", math_utils.exception_handling_demo()

if __name__ == '__main__':
    main()
