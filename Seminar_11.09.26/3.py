data = input()
n = len(data)

dict = {
    "A" : "A",
    "H" : "H",
    "I" : "I",
    "M" : "M",
    "O" : "O",
    "T" : "T",
    "U" : "U",
    "V" : "V",
    "W" : "W",
    "X" : "X",
    "Y" : "Y",
    "1" : "1",
    "8" : "8",
    "E" : "3",
    "J" : "L",
    "S" : "2",
    "Z" : "5",
    "5" : "Z",
    "2" : "S",
    "L" : "J",
    "3" : "E",
}

fl1 = 1
for i in range(len(data) // 2 + 2):
  if data[i] != data[n - 1 - i]:
    fl1 = 0
    break

fl2 = 1
for i in range(len(data) // 2 + 2):
  if data[i] in dict.keys():
    if data[n - i - 1] != dict[data[i]]:
      fl2 = 0
  else:
      fl2 = 0

if fl1 == 0 and fl2 == 0:
  print(f"{data} is not a palindrome.")
elif fl1 == 1 and fl2 == 0:
  print(f"{data} is a regular palindrome.")
elif fl1 == 1 and fl2 == 1:
  print(f"{data} is a mirrored palindrome.")
elif fl1 == 0 and fl2 == 1:
  print(f"{data} is a mirrored string.")
