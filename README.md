# Table of Contents

1. [Exercise 1](#exercise-1)
2. [Exercise 2](#exercise-2)
3. [Exercise 3](#exercise-3)
4. [Exercise 4 Part 1](#exercise-4-part-1)
5. [Exercise 4 Part 2](#exercise-4-part-2)
6. [Exercise 4 Part 3](#exercise-4-part-3)
7. [Exercise 5](#exercise-5)
8. [Exercise 6 Part 1](#exercise-6-part-1)
9. [Exercise 6 Part 2](#exercise-6-part-2)
10. [Exercise 6 Part 3](#exercise-6-part-3)
11. [Exercise 6 Part 4](#exercise-6-part-4)
12. [Exercise 6 Part 5](#exercise-6-part-5)
13. [Exercise 6 Part 6](#exercise-6-part-6)
14. [Exercise 6 Part 7](#exercise-6-part-7)
15. [Exercise 7 Part 1](#exercise-7-part-1)
16. [Exercise 7 Part 2](#exercise-7-part-2)
17. [Exercise 7 Part 3](#exercise-7-part-3)
18. [Exercise 7 Part 4](#exercise-7-part-4)
19. [Exercise 7 Part 5](#exercise-7-part-5)

# Exercise 1

## Table of Contents

1. [Install Python](#install-python)
2. [Set Up a Virtual Environment](#set-up-a-virtual-environment)
3. [Create a Python Script](#create-a-python-script)
4. [Set Up IPython Shell](#set-up-ipython-shell)
5. [Export a Requirements File](#export-a-requirements-file)
6. [Create a Github Repo](#create-a-github-repo)

## Install Python

First, install Python 3.8.7 on your system. Check your Python version by using the command `python --version` from your terminal.

![Step 1](./exercise1.1/1.png)

## Set Up a Virtual Environment

Set up a new virtual environment named “cf-python-base”.

![Step 2](./exercise1.1/2.png)

## Create a Python Script

Install Visual Studio Code or another text editor of your choice and create a Python script named “add.py”. This script will take two numbers from the user input, add them, and print the result. Here's the template for your Python script:

![Step 3](./exercise1.1/3.png)

```python
# Prompt the user to enter the first number
a = int(input("Enter the first number: "))

# Prompt the user to enter the second number
b = int(input("Enter the second number: "))

# Add the two numbers and store the result in variable c
c = a + b

# Print the value of c
print("The sum of", a, "and", b, "is:", c)
```

## Set Up IPython Shell

Set up an IPython shell in the virtual environment "cf-python-base". An IPython shell is similar to the regular Python REPL with additional features like syntax highlighting, auto-indentation, and robust auto-complete features. Install it using pip.

![Step 4](./exercise1.1/4.png)

## Export a Requirements File

Generate a “requirements.txt” file from your source environment. Next, create a new environment called “cf-python-copy”. In this new environment, install packages from the “requirements.txt” file.

![Step 5](./exercise1.1/5.png)

# Exercise 2

## Table of Contents

1. [Create the Data Structure](#create-the-data-structure)
2. [Create recipe_1](#create-recipe_1)
3. [Create Outer Structure](#create-outer-structure)
4. [Create 4 More Recipes](#create-4-more-recipes)
5. [Print Ingredient Lists](#print-ingredient-lists)

## Create the Data Structure

- Create a structure named recipe_1 that contains the following keys:
  - name (str): Contains the name of the recipe
  - cooking_time (int): Contains the cooking time in minutes
  - ingredients (list): Contains a number of ingredients, each of the str data type

![step 1](./exercise1.2/1.png)

_A dictionary is well-suited because it offers a key-value structure to link recipe attributes, making it simple to retrieve specific details using keys. It can store various data types, such as strings for the recipe name, integers for cooking time, and lists for ingredients. This structure ensures organization and consistency, which is especially beneficial when managing multiple recipes within a list. In summary, a dictionary allows for easy manipulation and structured access to recipe information, supporting further processing and analysis efficiently._

## Create recipe_1

![step 2](./exercise1.2/2.png)

## Create outer Structure

Create an outer structure called all_recipes, and then add recipe_1 to it.

![step 3](./exercise1.2/3.png)

_A list offers a flexible and dynamic structure, allowing for easy updates and retrieval of recipes based on their sequence. With support for iteration and indexing, it facilitates efficient operations on both individual recipes and the whole collection. Lists can handle recipes of different lengths and complexities, making them adaptable to a wide variety of recipe formats. In summary, a list provides the scalability, flexibility, and accessibility needed for effectively managing and modifying multiple recipes._

## Create 4 More Recipes

Generate 4 more recipes as recipe_2, recipe_3, recipe_4, and recipe_5, and then add them as well to all_recipes.

![step 4](./exercise1.2/4.png)

## Print Ingredient Lists

Print the ingredients of each recipe as five different lists, inside the IPython shell.

![step 5](./exercise1.2/5.png)

# Exercise 3

## Table of Contents

1. [Create a New Python Script](#create-a-new-python-script)
2. [Initialize Two Empty Lists](#initialize-two-empty-lists)
3. [Define a Function](#define-a-function)
4. [Get The Number of New Recipes](#get-the-number-of-new-recipes)
5. [Check Ingredients and Add Recipes](#check-ingredients-and-add-recipes)
6. [Assign Difficulty Levels and Display Recipes](#assign-difficulty-levles-and-display-recipes)
7. [Display All Ingredients](#display-all-ingredients)

## Create a New Python Script

Open a Python script in an editor of your choice and name it “Exercise_1.3.py”.

![step 1](./exercise1.3/1.png)

## Initialize Two Empty Lists

Initialize two empty lists: recipes_list and ingredients_list.

![step 2](./exercise1.3/2.png)

## Define a Function

Define a function called `take_recipe`, which takes input from the user for the following variables:

- `name` (str): Stores the name of the recipe.
- `cooking_time` (int): Stores the cooking time (in minutes).
- `ingredients` (list): A list that stores ingredients, each of the string data type.
- `recipe` (dictionary): Stores the `name`, `cooking_time`, and `ingredients` variables (e.g., `recipe = {'name': name, 'cooking_time': cooking_time, 'ingredients': ingredients}`).

![step 3](./exercise1.3/3.png)

## Get the Number of New Recipes

Ask the user how many recipes they would like to enter. Their response will be linked to a variable n.

![step 4](./exercise1.3/4.png)

## Check Ingredients and Add Recipes

Run a for loop, which runs n times to perform the following steps:

- Run `take_recipe()` and store its return output (a dictionary) in a variable called **recipe**.
- Run another for loop inside this loop, which iterates through recipe’s ingredients list, where it picks out elements one-by-one as ingredient. It will run the following step inside: if the chosen ingredient isn’t present in ingredients_list, add it to this list.
- Once finished adding ingredients, append recipe to recipes_list.

![step 5](./exercise1.3/5.png)

## Assign Difficulty Levels and Display Recipes

Run another for loop that iterates through the recipes_list and assign a difficulty level based on the following criteria:

- If cooking_time is less than 10 minutes, and the number of ingredients is less than 4, set a variable called difficulty to the value of **Easy**.
- If cooking_time is less than 10 minutes, and the number of ingredients is greater than or equal to 4, set a variable called difficulty to the value of **Medium**.
- If cooking_time is greater than or equal to 10 minutes, and the number of ingredients is less than 4, set a variable called difficulty to the value of **Intermediate**.
- If cooking_time is greater than or equal to 10 minutes, and the number of ingredients is greater than or equal to 4, set a variable called difficulty to the value of **Hard**.

Display each recipe in the following format:

- Recipe:
- Cooking Time (min):
- Ingredients:
- Difficulty level:

![step 6](./exercise1.3/6.png)

## Display All Ingredients

Display all the ingredients that you’ve come across so far in all of the recipes that you’ve entered.

![step 7](./exercise1.3/7.png)

# Exercise 4 Part 1

## Table of Contents

1. [Import Pickle Module](#import-pickle-module)
2. [Define the Take Recipe Function](#define-the-take-recipe-function)
3. [Define the Calc Difficulty Function](#define-the-calc-difficulty-function)
4. [Try To Open a File](#try-to-open-a-file)
5. [Take Additional Recipes](#take-additional-recipes)
6. [Create the Data Dictionary](#create-the-data-dictionary)
7. [Save Data to a File](#save-data-to-a-file)

## Import Pickle Module

![step 1](./exercise1.4/1.1.png)

## Define the Take Recipe Function

Define a function called `take_recipe()` to take recipes from the user, which performs the following operations:

- Taking in the recipe name, cooking time, and ingredients from the user.
- Calculating the difficulty of the recipe by calling the `calc_difficulty()` function.
- Gathering all these attributes into a dictionary and returning it.

![step 2](./exercise1.4/1.2.png)

## Define the Calc Difficulty Function

Define the function `calc_difficulty()`, where the difficulty is returned as **Easy**, **Medium**, **Intermediate** or **Hard** based on the following logic:

- If cooking_time is less than 10 minutes and the number of ingredients is less than 4, set a variable called difficulty to the value of **Easy**.
- If cooking_time is less than 10 minutes and the number of ingredients is greater than or equal to 4, set a variable called difficulty to **Medium**.
- If cooking_time is greater than or equal to 10 minutes and the number of ingredients is less than 4, set a variable called difficulty to the value of **Intermediate**.
- If cooking_time is greater than or equal to 10 minutes and the number of ingredients is greater than or equal to 4, set a variable called difficulty to **Hard**.

![step 3](./exercise1.4/1.3.png)

## Try To Open a File

Have a user enter a filename which would attempt to open a binary file in read mode, then define a try-except-else-finally block as follows:

- The **try** block will open the given file, and load its contents through the pickle module into a variable called data. The incoming data is expected to be a dictionary containing two key-value pairs:
  - recipes_list (a list of all recipes)
  - all_ingredients (a list of all ingredients across all recipes)
- An **except** clause handles the FileNotFoundError exception if a file with the given name isn’t found. The code block after will create a new dictionary called data, which contains the recipes list under the key recipes_list and another list containing all the ingredients under all_ingredients.
- Another **except** clause that handles other exceptions and performs the same operations as the first except block.
- An **else** block that closes the file stream that would’ve been opened in the try block.
- A **finally** block that extracts the values from the dictionary into two separate lists: recipes_list and all_ingredients.

![step 4](./exercise1.4/1.4.png)

## Take Additional Recipes

Ask the user how many recipes they’d like to enter, and define a for loop that calls the `take_recipe()` function. Append the output of this function into **recipes_list**. Next, define an inner loop that scans through the recipe’s ingredients and adds them to **all_ingredients** if they’re not already there.

![step 5](./exercise1.4/1.5.png)

## Create the Data Dictionary

Gather the updated `recipes_list` and `all_ingredients` into the dictionary called **data**.

![step 6](./exercise1.4/1.6.png)

## Save Data to a File

Open a user-defined binary file and write `data` to it using the pickle module.

![step 7](./exercise1.4/1.7.png)

# Exercise 4 Part 2

## Table of Contents

1. [Import the Pickle Module](#import-the-pickle-module)
2. [Define the Display Recipe Function](#define-the-display-recipe-function)
3. [Define the Search Ingredient Function](#define-the-search-ingredient-function)
4. [Ask User for Recipe File](#ask-user-for-recipe-file)
5. [Try To Open User File](#try-to-open-user-file)
6. [Create Except Block](#create-except-block)
7. [Create Else Block](#create-else-block)

## Import the Pickle Module

Import the pickle module:

![step 1](./exercise1.4/2.1.png)

## Define the Display Recipe Function

The function should take in one recipe (of the dictionary type) as an argument and print all of its attributes including the recipe name, cooking time, ingredients, and difficulty.

![step 2](./exercise1.4/2.2.png)

## Define the Search Ingredient Function

The function takes in a dictionary called data as its argument. The function will perform the following steps:

- First, it shows the user all the available ingredients contained in data, under the key all_ingredients. Each ingredient is displayed with a number (take the index of each ingredient for this purpose using the enumerate() function).
- Define a try block where the user gets to pick a number from this list. This number is used as the index to retrieve the corresponding ingredient, which is then stored into a variable called ingredient_searched.
- Make an except clause that warns the user if the input is incorrect.
- Add an else clause that goes through every recipe in data (hint: recipes_list is the key that holds every recipe). Each recipe that contains the given ingredient will be printed.

![step 3](./exercise1.4/2.3.png)

## Ask User for Recipe File

Ask the user for the name of the file that contains your recipe data.

![step 4](./exercise1.4/2.4.png)

## Try To Open User File

Use a `try` block to open the file, and then extract its contents into **data** (from Step 3) using the pickle module.

![step 5](./exercise1.4/2.5.png)

## Create Except Block

For when the try block fails, add an `except` block to warn the user that the file hasn’t been found.

![step 6](./exercise1.4/2.6.png)

## Create Else Block

Define an `else` block that calls `search_ingredient()` while passing `data` into it as an argument.

![step 7](./exercise1.4/2.7.png)

# Exercise 4 Part 3

## Table of Contents

1. [Run the Input Script](#run-the-input-script)
2. [Run the Search Script](#run-the-search-script)

## Run the Input Script

Run “recipe_input.py” and enter a few sample recipes of your choice. Make sure the script can generate a binary file after execution.

![step 1a](./exercise1.4/3.1.png)

## Run the Search Script

TO BE ADDED
