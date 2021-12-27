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
            # Call leaves behind a bookmark so you can return.
            call okay_choice
        "Puzzle":
            call okay_choice
        "Narrative":
            e "Heck yeah, I want to make a narrative game."
    e "We made a choice about what kind of game to make."
    return

label okay_choice:
    e "Eh, I guess, that's an okay choice."
    return
