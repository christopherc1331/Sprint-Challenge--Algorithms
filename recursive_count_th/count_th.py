'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    count = 0
    two_chars = ""

    if len(word) != 0:
        two_chars = word[0:2]
        rest = word[1:]
        if len(rest) >= 2:
            count += count_th(rest)
    if two_chars == "th":
        count += 1

    return count
