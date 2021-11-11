import part1, part2
import os

program = input("Which part? ")

while program not in ["1", "2"]:
  os.system('clear')
  print("That's not a valid input.")
  program = input("Which part? ")

if program == "1":
  n = int(input("Enter a number: "))
  print("The sum of the first " + str(n) + " squares is " + str(part1.sumofsquares(n)))

elif program == "2":
  s = int(input("Enter diamond size: "))
  print(part2.diamond(s))