def reverse_string(str):
    reverse_str = ""

    for s in str:
        reverse_str += str[-1]
        str = str[:-1]

    return reverse_str


def reverse_words(str):
    reverse_wrd = ""

    for s in str.split(" "):
        reverse_wrd += reverse_string(s) + " "

    return reverse_wrd.strip()


def reverse_word_order(str):
    reverse_str = ""

    str_list = str.split(" ")

    for s in reversed(str_list):
        reverse_str += s + " "

    return reverse_str.strip()