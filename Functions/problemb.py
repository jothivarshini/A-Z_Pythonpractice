def displayVerse(n):
    print("One the", intToOrdinal(n), "day of Christmas")
    print("my true sent to me:")

    if n >= 12:
        print("Twelve drummers drumming,")
    if n >= 11:
        print("Elevent pipers piping,")
    if n >= 10:
        print("Ten lords a leaping,")
    if n >= 9:
        print("Nine ladies dancing,")
    if n >= 8:
        print("Eight maids a milking,")
    if n >= 7:
        print("Seven swans a swimming,")
    if n >= 6:
        print("Six geese a laying,")
    if n >= 5:
        print("Five golden rings,")
    if n >= 4:
        print("Four calling birds,")
    if n >= 3:
        print("Three French hens,")
    if n >= 2:
        print("Two turtle doves,")
    if n == 1:
        print("A", end=" ")
    else:
        print("And a", end= " ")
    print("partrige in a pear tree.")
    print()
