#!/usr/bin/python3
def no_c(my_string):
    return my_string.trnslate({ord(c): None for c in "cC"})