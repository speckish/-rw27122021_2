# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

image rain:
    zoom 0.5
    "images/rain_1.png"
    pause 0.15
    "images/rain_2.png"
    pause 0.15
    "images/rain_3.png"
    pause 0.5
    "images/rain_4.png"
    repeat

label start:
    # if you add a "bg room.png" to your images folder, it will overwrite this.
    scene bg room
    # if you add a "eileen happy.png" to your images folder, it will overwrite this.
    show eileen happy
    show rain
    e "We're coding for the first time now."
    e "Test line."
    e "Wee! So fun!"
    jump brainstorm

label brainstorm:
    e "I'm not sure what I should make a game about."

    call screen image_button_example
    "Wee, buttons!"
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
