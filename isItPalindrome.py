# A palindrome is a word that's spelled the same in both directions!

def ask():
    """Asks for a word to check"""
    val = input('Please enter your word to check!: ')
    return val


def check_val(val):
    """Compares val against rev_val"""
    palindrome = False
    val = val
    # print('val = ', val)
    rev_val = val[::-1]
    # print('rev_val = ', rev_val)
    if val == rev_val:
        palindrome = True
    else:
        pass

    if palindrome == True:
        print("Yep", val, ", that one is a palindrome!")
    else:
        print("Nope", val, ", is not a palindrome!")
    print(palindrome)
    exit()


asked = ask()
# print(asked)
check_val(asked)
# print(check_val)

