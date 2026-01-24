collection = ["Кристалл", "Кольцо", "Кристалл", "Сфера", "Медальон"]

a_1 = input()

print(collection.count(a_1))

a_2 = input()

print(collection.index(a_2))

collection.sort()

print(collection)

collection.reverse()

print(collection)

collection_2 = collection.copy()

print(collection_2)
