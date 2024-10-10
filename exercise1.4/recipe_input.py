import pickle

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

def calc_difficulty(recipe):
  if recipe["cooking_time"] < 10 and len(recipe["ingredients"]) < 4:
    difficulty = "Easy"
  elif recipe["cooking_time"] < 10 and len(recipe["ingredients"]) >= 4:
    difficulty = "Medium"
  elif recipe["cooking_time"] >= 10 and len(recipe["ingredients"]) <= 4:
    difficulty = "Intermediate"
  else:
    difficulty = "Hard"
  return difficulty

filename = input("Enter the filename where you have stored your recipes: ")
try:
  with open(filename, "rb") as file:
    data = pickle.load(file)
    print("Recipes loaded successfully")
except FileNotFoundError:
  print("File does not exist -creating new file")
  data = {"recipes_list": [], "all_ingredients": []}
except:
  print("An unexpected error occured.")
  data = {"recipes_list": [], "all_ingredients": []}
else:
  file.close()
finally:
  recipes_list = data["recipes_list"]
  all_ingredients = data["all_ingredients"]

#get number of recipes from user
n = int(input("How many recipes would you like to enter? "))

#take recipes and add(append) to recipes_list
for i in range(n):
  recipe = take_recipe()

  #update all_ingredients with new ingredients
  for ingredient in recipe["ingredients"]:
    if ingredient not in all_ingredients:
      all_ingredients.append(ingredient)

  #add recipe to recipe_list
  recipes_list.append(recipe)

#save the recipes_list and all_ingredients to a dictionary
data = {"recipes_list": recipes_list, "all_ingredients": all_ingredients}

#save dicitonary to user-specified file
filename = input("Enter the filename where you would like to store your recipes: ")
with open(filename, "wb") as file:
  pickle.dump(data, file)
  print("Recipes saved successfully!")
  file.close()