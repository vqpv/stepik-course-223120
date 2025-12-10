print((a := input())[0].isupper() and a.replace("_", "").isalnum() and len(a) <= 20)
