import random

words = ['Python', 'Java', 'C++', 'Ruby', 'Nodejs', 'PHP', 'Laravel', 'Reactjs', 'HTML', 'SQL', 'ASP', 'Git']

print(words, "\n")
print("\nGuess the word from the given list\n")

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
# list the words using for loop to get char length
for word in words:
  word = random.choice(words)

# get the length of a random word
# get the index to print the hint for the random word
hint = words.index(word)
print("Hint:", hints[hint] + ", Word has",len(word), "characters")


lives = 5
print("\nNote: You have 5 lives to guess\n")

# guessing loop according to number of lives
while lives > 0:
  userAns = input()
  if userAns == word:
    print("Awesome, You won !")
    break
  else:
    lives = lives - 1
    print("Wrong Guess! You have ", lives, "remaining lives\n")
else:
  print("You lose")
