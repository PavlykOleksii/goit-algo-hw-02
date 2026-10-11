from collections import deque

def is_palindrome(text: str) -> bool:
    text = text.lower().replace(" ","")
    frase = deque(text)
    while len(frase) > 1:
        if not frase.pop() == frase.popleft():
            return False
    return True


print(is_palindrome("Я несу гусеня"))
print(is_palindrome("Я несу гусеня!"))