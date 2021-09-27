#integers dont need quotations
#you can do math 
print(100 + 65)
print(77 * 55)
print(76 / 44)
print(69 // 5)
print("100" + "100")
print("cat" + "dog")
print("cat" * 10)

print("-------------------")

def madLib(instrument, number, dayorweek, letter, majororminor, number1, number2, adj1, adj2, fraction, adj3, instrument2, adj4, noun, familymember, song, adjendingined, favartist):
    
    print("While I've stayed at home, I've practiced the " + instrument + " for " + number + " hours every " + dayorweek + ". My favorite key signature to play and practice in is " + letter + majororminor + ". It has " + number1 + " flats and " + number2 + " sharps. I like this key signature because it is " + adj1 + " and " + adj2 + ". I've also gotten awesome at counting time signatures. The time signature I love is " + fraction + " , because it is " + adj3 + " to count. One instrument I want to learn how to play while I'm at home is " + instrument2 + " , because it is " + adj4 + " and sounds like a " + noun + " . my " + familymember + " likes it when I play " + song + " , and always gives me a round of applause after my performances! when I return to school, my teacher will be " + adjendingined + " of how great I am at playing my instrument. My teacher might even think I sound like " + favartist + "!")

madLib("piano", "24", "tuesday", "A ", "major", "six", "seven", "cool", "awesome", "1/5", "hard", "guitar", "interesting", "cat", "mom", "status", "astonished", "NAV")


print("-------------------")

def color():
    return "red"

print(color() + " is my favorite color")

print("-------------------")

def greaterThan10(x):
    if  x > 10: 
        return "x is greater than 10"

    elif x == 10:
        return "x equals 10"

    else:
        return "x is not greater than 10" 



print(greaterThan10(10))


def potato(x, y):
    if x + y > 10:
        return "potato"

    elif x + y == 10:
        return "tomato"

    else:
        return "alfredo"

print(potato(5, 1))


if "cat" < "dog":
    print("wow I can't believe this worked")

else:
    print("wow I still can't believe this worked")

def login(password):
    if password == "OsowskiR00lz":
        return "access granted"

    else:
        return "access denied"

print(login("OsowskiR00lz"))




def trivia(answer):
    if answer.lower() == "gerald":
        return "bingo"
    
    

    else:
        "git good lol"

print(trivia("GerAld"))

print("gerald".upper())

def fiveSauces(sauce):
    
    sauce = sauce.lower()    
    
    if sauce == "tomato":
        return "Bingo!"

    elif sauce == "mayonaise":
        return "Bingo!"
    
    elif sauce == "bechemel":
        return "Bingo!"

    elif sauce == "espagnole":
        return "Bingo!"

    else:
        return "uncultured swine"

print(fiveSauces("Tomato"))

def define(word):
    word = word.lower()
    if word == "snake":
        return "snake: a long, slithery creature"

    elif word == "jungle":
        return "a place that is hot with a lot of trees"

    elif word == "car":
        return "car: a moving vehicle that has 4 wheels"

    elif word == "donut":
        return "donut: a very good circular food"

    elif word == "grass":
        return "grass: green stuff that is on the ground"

    elif word == "wow":
        return "wow: something you say when you are amazed"

    elif word == "pencil":
        return "pencil: a thing you write with"

    elif word == "run":
        return "run: a way for humans to move faster than walking"

    elif word == "jump":
        return "jump: a way for humans to get off the ground"

    elif word == "game":
        return "game: fun things humans play"

    else:
        return "that word is not reconised in this dictionary"

print(define("JUmp"))