def guess(args, dictionary: list):
    temp_dictionary = dictionary.copy()
    if len(args) != 2:
        return print("Invalid args for guess command.")

    word = list(args[0])
    hint = list(args[1])

    print("Reduced list from:", len(temp_dictionary), "words to")
    for entry in dictionary: #regis
        for i in range(len(word)):
            letter = word[i]
            if(hint[i] == '+'):
                if(entry[i] != letter):
                    temp_dictionary.remove(entry)
                    break
            if(hint[i] == '?'):
                if(entry[i] == letter or letter not in entry):
                    temp_dictionary.remove(entry)
                    break
            elif(hint[i] == '-'):
                if(letter in entry):
                    temp_dictionary.remove(entry)
                    break

    dictionary = temp_dictionary.copy()

    print(len(temp_dictionary), "words")
    print(temp_dictionary)

    return temp_dictionary

def help():
    return ("guess <word> <hint>\n"+

    "`word` is the given word that was entered into the wordle. (ie, earth)\n"+

    "`hint` is a specially formatted guess string based on the results of the guess. The valid characters are + - and ?, and replace the letters of the word.\n"+
    
    "+ is to be used if a letter exists and is in the right place.\n"+
    "? is to be used if a letter exists and is in the wrong place.\n"+
    "- is to be used if a letter does not exist.\n\n"+
    "example: word is EARTH. E is in the word. A is in the word, but not in the right spot. R T and H are not in the word at all. The hint string should look like +?---\n"+
    "ie: `guess earth +?---`"
    )