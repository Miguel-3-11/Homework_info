def intag(tag: str, text: str) -> str:
    tags = {
        'a', 'abbr', 'b', 'body', 'caption', 'cite', 'code', 'div',
        'form', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'header', 'i', 's'
    }

    if tag in tags:
        return f"<{tag}>{text}</{tag}>"
    return "Введён неверный тег"

tag = input().strip()
text = input().strip()

print(intag(tag, text))