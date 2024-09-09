#!/usr/bin/python3
"""This module have function for password
"""
import string
import random
def password_gen(length=8,digits=True,special_char=True):
    """function generates password

    Args:
        length (int, length): length for a password. Defaults to 8.
        digits (bool, digits):include digits. Defaults to True.
        special_char (bool, special_char):include special characters. Defaults to True.
    """
    pass_gen=""
    # adding letters,digits,special-char to a string
    total_char=string.ascii_letters
    total_char+=string.digits
    total_char+=string.punctuation
    # choosing random character and concating to string
    pass_gen+=random.choice(string.ascii_uppercase)
    pass_gen+=random.choice(string.ascii_lowercase)
    count=2
    if digits:
        pass_gen+=random.choice(string.digits)
        count+=1
    if special_char:
        pass_gen+=random.choice(string.punctuation)
        count+=1
    remain_str=""
    #for _ in range(int(len)-count):
        #remain_str+=random.choice(total_char)
    remain_str=[random.choice(total_char) for _ in range(int(length)-count)]
    # concating remaining string after certain conditions meet
    pass_gen+="".join(remain_str)

    return pass_gen





