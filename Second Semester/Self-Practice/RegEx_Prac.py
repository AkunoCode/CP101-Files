import re

def text_match(text):
    pattern = re.compile(r'\w')
    if re.search(pattern,  text):
        return 'Found a match!'
    else:
        return('Not matched!')

print(text_match("Abcds asdw"))
print(text_match("BABaaa"))
print(text_match("cDaaa"))
print(text_match("abbbc_ad_Ab"))
print(text_match("abbbb_b"))
