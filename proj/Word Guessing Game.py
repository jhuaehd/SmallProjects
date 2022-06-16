import random

words = ['Python', 'Java', 'C++', 'Ruby', 'Nodejs', 'PHP', 'Laravel']
print(words, "\n")
print("Guess the word from the given list")


for word in words:
  word = random.choice(words)
  
print("Word has ", len(word), "characters")

lives = 5
while lives > 0:
  userAns = input()
  if userAns == word:
    print("Awesome, You won !")
    break
  else:
    lives = lives - 1
    print("Wrong Guess! You have ", lives, "remaining lives")

else:
  print("You lose")
