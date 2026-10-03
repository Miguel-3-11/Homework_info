import string

with open('C:/Users/user/AppData/Local/Programs/Python/Python312/LICENSE.txt' , 'r', encoding='utf-8') as f:
    text = f.read()

for char in string.punctuation:
    text = text.replace(char, ' ')

words = text.lower().split()

word_cnt = {}

for word in words:
    word_cnt[word] = word_cnt.get(word, 0) + 1

print("10 самых часто употребляемых слов:")
for _ in range(10):
    max_word = max(word_cnt, key=word_cnt.get)
    print(f"{max_word}: {word_cnt.pop(max_word)}")