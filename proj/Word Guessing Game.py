import random
import sys
import time

words = [
    'Python', 'Java', 'C++', 'Ruby', 'Nodejs', 'PHP', 'Laravel', 'Reactjs',
    'HTML', 'SQL', 'ASP', 'Git'
]

print(words, "\n")
print("\nGuess the word from the given list\n")

hints = [
    'Snake', 'Root crop', 'Increment', 'Shining',
    'non-blocking, event-driven servers', 'Web Database',
    'an open-source PHP framework', 'a JavaScript library', 'Markup Language',
    'Query', 'development framework for building web pages',
    'an Open Source Distributed Version Control System'
]

# list the words using for loop to get char length
for word in words:
    # select random word from words
    word = random.choice(words)

# get the length of a random word
# get the index to print the hint for the random word
hint = words.index(word)

print("Hint:", hints[hint] + ", Word has", len(word), "characters")

guesses = 5
print("\nNote: You have 5 lives to guess\n")

# guessing loop according to number of lives
while guesses > 0:
    userAns = input()
    # timer
    for x in reversed(range(5)):
        # sys.stdout.write('\r' + str(x) + '\n')
        time.sleep(1)

        # user input
        if userAns == word:
            print("Awesome, You won !")
            break

        else:
            guesses = guesses - 1
            pass
            print("Wrong Guess! You have ", guesses, "remaining lives\n")

else:
    print("You lose")
