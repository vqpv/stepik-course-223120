s = input()

nums = list(map(int, s.split()))

if all((i > 0 for i in nums)):
    print("All positive")
elif any((i < 0 for i in nums)):
    print("Any negative")
else:
    print("Mixed or zero")
