print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("Youcan ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    print("Please pay $5")
  elif age <= 18:
    print("Please pay $7.")
  elif age > 22:
    print("Please pay $20.")
  elif height >= 180:
    print("Please pay $30.")
  else:
    print("Please pay $12.")
else:
  print("Sorry, you have to grow taller before you can ride.")