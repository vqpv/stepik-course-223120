ingredients = []

ingredients.append(input())
ingredients.extend(input().split(", "))
ingredients.insert(1, input())
ingredients.remove(input())
ingredients.pop()

print(ingredients)
