def reverseLookup(data, value):
    keys=[]

    for key in data:
        if data[key] == value:
            keys.append(key)
        return keys

def main():
    frEn{"le": "the", "la": "the", "livre": "book", "pomme": "apple"}

    print("The french words for 'the' are: "  reverseLookup (frEn, "the"))
    print ("expected:['le', 'la']")
    print()
    print("The french words for 'apple' is: "  reverseLookup (frEn, "apple"))
    print("expected:['pomme']")
