class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word+'('+self.meaning+')'
flash = []
print("welcome to flashcards")
while(True):
    word = input("Enter a word for your flashcard : ")
    meaning = input("Enter a meaning for your word : ")
    flash.append(flashcard(word,meaning))
    option = int(input("Enter 0 if you want to add another card. Enter 1 if you want to stop : "))
    if(option):
        break
    print("\n Your flashcards : ")
    for l in flash:
        print(">", l)