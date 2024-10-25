import pickle

def display_recipe(recipe):
  print("Recipe: ", recipe["name"])
  print("Cooking time (min): ", recipe["cooking_time"])
  print("Ingredients:")
  for ingredient in recipe["ingredients"]:
    print(ingredient)
  print("Difficulty: ", recipe["difficulty"])
  print()

def search_ingredient(data):
  print("Available ingredients:")
  for index, ingredient in enumerate(data["all_ingredients"]):
    print(index, ingredient)
  print()
  try:
    ingredient_searched = data["all_ingredients"][
      int(input("Enter the number of ingredients you want to search for: "))
    ]
  except:
    print("Incorrect input")
    return
  else:
    recipes_found = []
    for recipe in data["recipes_list"]:
      if ingredient_searched in recipe["ingredients"]:
        recipes_found.append(recipe)
    for recipe in recipes_found:
      display_recipe(recipe)

filename = input("Enter the filename where you have stored your recipes: ")

try:
  file = open(filename, "rb")
  data = pickle.load(file)
except FileNotFoundError:
  print("Warning, file has not been found")
else:
  search_ingredient(data)
finally:
  print("Goodbye!")
  file.close()
