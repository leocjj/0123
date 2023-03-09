s = "a c e g i k m o q s u w y"

# Write a function that takes a string as input and returns a list of strings
# where each string is a character from the input string.
#   Example: "abc" -> ["a", "b", "c"]
#   Example: "a c e g i k m o q s u w y" -> ["a", " ", "c", " ", "e", " ", "g", " ", "i", " ", "k", " ", "m", " ", "o", " ", "q", " ", "s", " ", "u", " ", "w", " ", "y"]
#   Example: "a c e g i k m o q s u w y" -> ["a", "c", "e", "g", "i", "k", "m", "o", "q", "s", "u", "w", "y"]

def split_string(s):
    # return s.split()
    # return list(s)
    # return [c for c in s]
    return list(map(lambda c: c, s))

def test_split_string():
    assert split_string("abc") == ["a", "b", "c"]
    assert not split_string("a c e g i k m o q s u w y") == ["a", "c", "e", "g", "i", "k", "m", "o", "q", "s", "u", "w", "y"]
    assert split_string("a c e g i k m o q s u w y") == ["a", " ", "c", " ", "e", " ", "g", " ", "i", " ", "k", " ", "m", " ", "o", " ", "q", " ", "s", " ", "u", " ", "w", " ", "y"]
    
test_split_string()