import re

f = open("input.txt", "r")
text = f.read()
f.close()
sentences = re.split(r'[.?!;]', text)
#Могут ли предложения быть разделены ; ?
cnt = 0
for el in sentences:
  if el != "":
    cnt += 1

print(cnt)