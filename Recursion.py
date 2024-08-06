Word = "WWWOOORLLLD"

def CleanWord(Word) :
    
    if (len(Word)) == 1 : return Word

    if (Word[0] == Word[1]) : return CleanWord(Word[1:])

    return Word[0] + CleanWord(Word[1:])

print(CleanWord(Word))


