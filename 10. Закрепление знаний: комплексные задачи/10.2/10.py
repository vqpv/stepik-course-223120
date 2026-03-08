s = input()

vowels = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я", "А", "Е", "Ё", "И", "О", "У", "Ы", "Э", "Ю", "Я"]

words = [w for w in s.split() if len(w) >= 3]
count = len(words)

if words:
    long_word = words[0]
    
    for word in words:
        if len(word) > len(long_word):
            long_word = word

    new_long_word = ""
    
    for i in long_word:
        if i not in vowels:
            new_long_word += i

print("Осталось слов длиной 3+ символа:", count)

if words:
    print("Самое длинное слово:", long_word)
    print("Самое длинное слово без гласных:", new_long_word)
