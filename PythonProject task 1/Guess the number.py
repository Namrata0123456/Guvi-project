import random
random_numbers = random.randrange(1,40)
guessed_numbers = int(input("please enter the number between 1 and 40: - "))
trial = 1
while trial <=3:
  if random_numbers == guessed_numbers:
    print("you guessed it right")
  elif random_numbers < guessed_numbers:
    print("you guessed higher number")
  else:
     print("you guessed lower number")
  trial+=1
  guessed_numbers = int(input("please enter the number between 1 and 40: - "))
print(f"trial over,better next time,the generated number is {random_numbers}")