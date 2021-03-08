################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")
# local scope exists within a function

# def drink_potion():
#   potion_strength = 2
#   print(potion_strength)

# drink_potion()
# print(potion_strength)

#Global Scope
player_health = 10 #global var

def drink_potion():
  potion_strength = 2  # local var
  print(player_health)

drink_potion()