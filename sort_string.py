# Write a Python function to sort the words in a string.
# Input: string of words seperated by spaces
# Output: string of words sorted alphabetically


def get_string_input():
    """Ask the user for some words, store as a string and return"""
    answer = input("OK give me a string of words, seperated by spaces: ")
    return answer


def create_list_of_words(answer):
    """From the return of input string, break the single string into a list using the spaces as
    a delimiter, return the list of words"""
    # answer = answer
    words = answer.split()
    return words


def re_order_words(words):
    """From (create_list_of_words) Re-order the list, then print the result to the console"""
    print(type(words))
    new_words = words.sort()
    return new_words


ask = get_string_input()

while ask is None:
    ask = get_string_input()
    print(ask)
else:
    print("Well we got this far", "ask = ", ask)
    print(type(ask))
    the_words = create_list_of_words(ask)
    re_order_words(the_words)
    print(type(the_words))
    for i in the_words:
        print(i)


# The short version from demo
# def sort_words(input):
#   return ' ' .join(sorted(input.split(), key = str.casefold))
