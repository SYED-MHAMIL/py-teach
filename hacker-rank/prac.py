def reverse_chars_keep_digits(s):
    char = [c for c in s if not c.isdigit()]
    result = ""
    for c in s:
        if(c.isdigit()):
            result+=c

        else:
            result+=char.pop()
    return result

print(reverse_chars_keep_digits("1ali2"))