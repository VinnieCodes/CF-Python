recipes_list = []
ingredients_list = []

def take_recipe():
  name = input("Enter the name of the recipe: ")
  cooking_time = int(input("Enter the cooking time: "))
  ingredients = []
  while True: 
    ingredient = input(
      "Enter an ingredient (or enter 'done' if you have finished): "
    )
    if ingredient == "done": 
      break
    else:
      ingredients.append(ingredient)
  recipe = {"name": name, "cooking_time": cooking_time, "ingredients": ingredients}
  return recipe

n = int(input("How many recipes would you like to enter? "))

for i in range(n):
  recipe = take_recipe()
  for ingredient in recipe["ingredients"]:
    if ingredient not in ingredients_list:
      ingredients_list.append(ingredient)
  recipes_list.append(recipe)

for recipe in recipes_list:
  if recipe["cooking_time"] < 10 and len(recipe["ingredients"]) < 4:
    recipe["difficulty"] = "Easy"
  elif recipe["cooking_time"] < 10 and len(recipe["ingredients"]) >= 4:
    recipe["difficulty"] = "Medium"
  elif recipe["cooking_time"] >= 10 and len(recipe["ingredients"]) <= 4:
    recipe["difficulty"] = "Medium"
  else:
    recipe["difficulty"] = "Hard"

for recipe in recipes_list:
  print("Recipe: ", recipe["name"])
  print("Cooking time (min): ", recipe["cooking_time"])
  print("Ingredients:")
  for ingredient in recipe["ingredients"]:
    print(ingredient)
  print("Difficulty: ", recipe["difficulty"])
  print()

print("Ingredients available across all recipes")
print("----------------------------------------")

ingredients_list.sort()

for ingredient in ingredients_list:
  print(ingredient)