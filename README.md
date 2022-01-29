# Wordle Solver
A very basic python tool to *help* guess possible wordle words. Automates the process of thinking up valid words based on guesses. Though arguably, that is the point of the game, so this is more of an exercise in programming than it is something to be used, but could help if you're really stuck.

## Setup
I reccomend installing the requirements in a virtual environment.

> pip install -r requirements.txt

Once installed run `wordle.py` via python. 

> python wordle.py

> Note: this currently uses the `english-words` pip library, which may or may not actually have some of the words that wordle uses. Notably plural words may be absent.

## Commands
`guess <word> <hint string>`: Takes two arguments. The word and a custom "hint string" which consists of `+ -` or `?`, based on the result of the wordle hint. Example:
* `guess alter -?--+`
* The word 'alter' was guessed. The actual wordle word does contain an r at the 5th position, contains an l in a different spot than the second position, and does not contain the letters a, t, e at all.
* It will return a whole list of words to use. Each time you use the `guess` command, the list will be narrowed down further.

`wordles`: Prints the list of possible words.

`exit`: exits the program.

`help`: Prints out how to use `guess`