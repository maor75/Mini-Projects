import random

def win(word1):
    for i in word1:
        if i == "_":
            return True
    return False

def display(word2):
    word2 = " ".join(word2)
    return word2

def dup(c, word3):
    for i in word3:
        if i == c:
            return False
    return True

        
opt = ["deny", "smart", "random", "melon","maor","game","banana"]
word = list(opt[(random.randint(0, len(opt) - 1))])

hidden = []
for i in word:
    hidden.append("_")
print(display(hidden))

right = False
nog = 10 #number of guesses
while nog > 0 and win(hidden):
    guess = input("enter your guess: ")
    if dup(guess, hidden):
        for i in range(len(word)):
            if guess == word[i]:
                hidden[i] = guess
                right = True
        if right == False:
            nog -= 1
        right = False
        print(display(hidden))
        print(f"you have {nog} left")
    else:
        print("you've tried that one already")
if not win(hidden):
    print("Winner winner chicken dinner!")
elif nog == 0:
    print("Game Over! better luck next time")
