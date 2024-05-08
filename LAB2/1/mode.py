def main(words, f):
    if not words:
        print("The list is empty.")
        return 0
    else:
        # Input the text, convert its to words to uppercase, and
        # add the words to a list
        for line in f:
            wordsInLine = line.split()
            for word in wordsInLine:
                words.append(word.upper())

        # Obtain the set of unique words and their
        # frequencies, saving these associations in
        # a dictionary
        theDictionary = {}
        for word in words:
            number = theDictionary.get(word, None)
            if number == None:
                # word entered for the first time
                theDictionary[word] = 1
            else:
                # word already seen, increment its number
                theDictionary[word] = number + 1

        # Find the mode by obtaining the maximum value
        # in the dictionary and determining its key
        theMaximum = max(theDictionary.values())
        for key in theDictionary:
            if theDictionary[key] == theMaximum:
                print("The mode is", key)
                break
