import utils.string_utils as su


def test_say_hello():
    assert su.say_hello("Alice") == "Hello, Alice!"

def test_count_words():
    result = su.count_words("Hello hello world")
    assert result["hello"] == 2
    assert result["world"] == 1

def test_string_io_example():
    output = su.string_io_example()
    assert "string buffer" in output

def test_dictionary_iteration():
    output = su.dictionary_iteration()
    assert "a => 1" in output
    assert "b => 2" in output
