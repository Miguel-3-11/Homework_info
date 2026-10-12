def ascii(s: str) -> int:
    l = len(s)

    if l <= 2:
        return ord(s[0])
    elif l < 10:
        first = ord(s[0])
        mid = ord(s[(l - 1) // 2])
        last = ord(s[-1])
        return first + mid + last
    else:
        return ord(s[-1])

text = input()
print(ascii(text))