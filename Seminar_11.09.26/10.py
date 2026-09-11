f = open("input.txt", "r")
text = list(f.read())
f.close()


lets = "УуЕеЫыАаОоЭэЯяИиЁёЮю"

for i in range(len(text)):
  if i > 0 and i < len(text) - 1:
    if text[i] in lets and text[i - 1][-1] not in lets and text[i + 1][-1] not in lets:
      text[i] = f"{text[i]}с{text[i]}"
    elif text[i] in lets and text[i - 1][-1] not in lets and text[i + 1][-1] in lets:
      text[i] = f"{text[i]}с{text[i]}"
  elif i == 0:
    if text[i] in lets and text[i + 1][-1] not in lets:
      text[i] = f"{text[i]}с{text[i]}"
    elif text[i] in lets and text[i + 1][-1] in lets:
      text[i] = f"{text[i]}с{text[i]}"
  elif i == len(text) - 1:
    if text[i] in lets and text[i - 1][-1] not in lets:
      text[i] = f"{text[i]}с{text[i]}"

print(''.join(text))