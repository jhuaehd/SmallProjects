import random

words = ['Python', 'Java', 'C++', 'Ruby', 'Nodejs', 'PHP', 'Laravel', 'Reactjs', 'HTML', 'SQL', 'ASP', 'Git']

print(words, "\n")
print("\nGuess the word from the given list")

hints = ['Snake', 
         'Root crop',
         'Increment',
         'Shining',
         'non-blocking, event-driven servers',
         'Web Database',
         'an open-source PHP framework',
         'a JavaScript library',
         'Markup Language',
         'Query',
         'development framework for building web pages',
         'an Open Source Distributed Version Control System'
        ]

# list the words using for loop
for word in words:
  word = random.choice(words)

# get the length of a random word
hint = words.index(word)
print("Hint:(", hints[hint] + "),Word has",len(word), "characters")
# get the index to print the hint for the random word

lives = 5
print("\nYou have 5 lives to guess, there's also a hint for you to guess faster.\n")

# guessing loop according to number of lives
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
