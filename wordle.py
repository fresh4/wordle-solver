from utils import set_wordles, set_letter_score, set_likely_words
from commands import guess, help

wordles = set_wordles()
alphabet_score = set_letter_score()
likely_words = set_likely_words(wordles, alphabet_score)

commands = ["guess", "wordles", "exit", "help", "restart", "r"]
active = True

while active:
    val = input("~").split(" ")
    cmd = val.pop(0)
    args = val

    if cmd in commands:
        if cmd == "guess":
            wordles = guess(args, wordles)
        if cmd == "wordles":
            print(wordles)
        if cmd == "exit":
            active = False
        if cmd == "restart" or cmd == "r":
            print("Starting new session:")
            wordles = set_wordles()
        if cmd == "help":
            print(help())
    else:
        print("Not a valid command.")