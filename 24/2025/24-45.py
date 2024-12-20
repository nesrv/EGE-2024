s = '''
ABBAAABBABBXY
XYYYXYAB
'''.split()

for sub_s in s:
    sub_s = sorted(sub_s, key=len)
    print(sub_s)