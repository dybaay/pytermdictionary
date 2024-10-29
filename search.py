import json
import difflib

def loadDictionaryContent():
    return json.load(open("dictionary.json"))

def searchDictionary(word):
    word = word.lower()
    dictionary = loadDictionaryContent()
    meaning = dictionary.get(word)
    response = ""
    if meaning:
        response = meaning
    else:
        closest_matches = difflib.get_close_matches(word, dictionary.keys(), 1, 0.8)
        if closest_matches:
            yN = input(f"Word not found. Did you mean '{closest_matches[0]}'. Enter Y if yes and N if no? ").lower()
            if yN == "y" or yN == "yes":
                return dictionary.get(closest_matches[0])
        else:
            response = "Word not found and no close matches available."
    return response

while True:
    word = input("Enter the word (enter \Q to quit the program): ")
    if word != "\Q":
        print(searchDictionary(word))
    else:
        break
