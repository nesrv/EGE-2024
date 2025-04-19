# s = "BBBBABBAAABBBBBABBABBBAABAAEABBFBBBBABBAAABEBAEBABABBAAABABBABABBA"
s = open("я-март-25-10/24.txt").read()

s = (
    s.replace("E", "A")
    .replace("C", "B")
    .replace("D", "B")
    .replace("F", "B")
    .split("AB")
)

max_s = 0

for i in range(len(s)):
    sub_s = s[i : i + 131]
    sub_s = "".join(sub_s)
    max_s = max(max_s, len(sub_s))

print(max_s + 262)

# 645
