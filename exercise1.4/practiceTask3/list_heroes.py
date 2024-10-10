def display(file):
  heroes = []
  for line in file:
    #removing newline characters
    line = line.rstrip("\n")

    #here we us the split(", ") method available to strings
    #to split the hero name and the year separately
    #the separation occurs at ", "

    #taking the first element of the split
    hero_name = line.split(", ")[0]
    #taking the second element of the split
    first_appearance = line.split(", ")[1]

    #we pack these two into a smaller, two-element
    #list, and then append it to the list "heroes"
    heroes.append([hero_name, first_appearance])

  #now, we will sort "heroes" by first appearance
  heroes.sort(key = lambda hero: hero[1])

  for hero in heroes:
    print("--------------------------------")
    print("Superhero: " + hero[0])
    print("First year of appearance: " + hero[1])

filename = input("Enter the filename where you have sorted your superheroes: ")
try:
  file = open(filename, 'r')
  display(file)
except FileNotFoundError:
  print("File does not exist - exiting")
except:
  print("An unexpected error occured.")
else:
  file.close()
finally:
  print("\n")
  print("Goodbye!")