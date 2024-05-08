import random

def getWords():
    with open("nouns.txt", 'r') as f:
        nouns = tuple(word for line in f for word in line.split())

    with open("articles.txt", 'r') as g:
        articles = tuple(word for line in g for word in line.split())

    with open("prepositions.txt", 'r') as h:
        prepositions = tuple(word for line in h for word in line.split())

    with open("verbs.txt", 'r') as i:
        verbs = tuple(word for line in i for word in line.split())

    return verbs, articles, nouns, prepositions


def sentence(verbs, articles, nouns, preposition):
    """Builds and returns a sentence."""
    return nounPhrase(articles, nouns) + " " + verbPhrase(verbs, articles, nouns, preposition)

def nounPhrase(articles, nouns):
    """Builds and returns a noun phrase."""
    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase(verbs, articles, nouns, prepositions):
    """Builds and returns a verb phrase."""
    return random.choice(verbs) + " " + nounPhrase(articles, nouns) + " " + \
           prepositionalPhrase(prepositions, articles, nouns)

def prepositionalPhrase(prepositions, articles, nouns):
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounPhrase(articles, nouns)

def main(verbs, articles, nouns, preposition):
    """Allows the user to input the number of sentences
    to generate."""
    number = int(input("Enter the number of sentences: "))
    getWords()
    for count in range(number):
        print(sentence(verbs, articles, nouns, preposition))

if __name__ == "__main__":
    verbs, articles, nouns, preposition = getWords()
    main(verbs, articles, nouns, preposition)
