s = input().strip()
sorte_chars = sorted(s)
result = "{" + ", ".join(f"'{char}'"for char in sorte_chars) + "}"
print(result)