def upper_string(s: str) -> str:
    if len(s) >= 4:
        upper_count = sum([1 for c in s[:4] if c.isupper()])
        if upper_count >= 3:
            return s.upper()
    if s and all(c.isupper() for c in s):
            return s.upper()
    return s

text = input()
print(upper_string(text))