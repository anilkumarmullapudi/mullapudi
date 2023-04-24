import re
# txt = "The rain is spain"
# print(txt)
# x = re.findall(r"ain\b",txt)

# print(x)

with open("C:\/Users\/anilk\/phonenumbers.txt") as phnum:
    for i in phnum:
        # x = re.findall('[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]', i)
        x = re.findall('[+][0-9][0-9] [0-9][0-9][0-9]-[0-9][0-9][0-9]-[0-9][0-9][0-9]', i)
        print(x)
