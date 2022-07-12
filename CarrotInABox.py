import random
p1Name = input("Enter player 1 name: ")
p2Name = input("Enter player 2 name: ")

print("""here are two boxes

  _________
 /        /|
+--------+ |
|        | |
|    A   | |
|        | /
+--------+/

  _________
 /        /|
+--------+ |
|        | |
|   B    | |
|        | /
+--------+/

""")

print("Rules rules rules")
input("Press enter when ready to open box A: ")
if random.randint(1, 2) == 1:
  carrotInA = True
else:
  carrotInA = False


if carrotInA:
  print("""
  
  
   __\/__
   \    / 
  __\  /___
 /   \/   /|
+--------+ |
|        | |
|    A   | |
|        | /
+--------+/


Your box contains THE CARROT
  """)
else:
  print("""
  
   _________
 /        /|
+--------+ |
|        | |
|    A   | |
|        | /
+--------+/
  

Your box contains NO CARROT
  """)


input("Press enter to continue: ")

print("\n" * 70)
print("player 2 can open their eyes")

p2Choice = input(p2Name + " Would you like to swap boxes? (y/n) ")

if p2Choice == "y":
  print("boxes swapped")
  carrotInA = not carrotInA
else:
  print("boxes not swapped")

input("Press enter to reveal the winner:  ")

if carrotInA:
  print(p1Name + " wins")
else:
  print(p2Name + " wins")
