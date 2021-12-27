# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:
    scene bg room
    show eileen happy
    e "We're coding for the first time now."
    e "Test line."
    e "Wee! So fun!"
    jump brainstorm

label brainstorm:
    e "I'm not sure what I should make a game about."
    menu:
        "Adventure":
            pass
        "Puzzle":
            pass
        "Narrative":
            pass
    e "We made a choice about what kind of game to make."
    return
