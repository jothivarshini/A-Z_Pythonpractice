s = input("Enter a string: ")
characters={}
for ch in s:
    characters[ch] = True

    print ("That string contained",len(characters), "uniquecharacter(s).")
