# Variables declarations for game characters and their stats
wizard = "Wizard"
elf = "Elf"
human = "Human"
orc = "Orc"

wizard_hp = 70
elf_hp = 100
human_hp = 150
orc_hp = 120
dragon_hp = 300

wizard_damage = 150
elf_damage = 100
human_damage = 20
orc_damage = 60
dragon_damage = 50

# Prompt the player to choose from a list of options
while True:
    print(f"1) {wizard}")
    print(f"2) {elf}")
    print(f"3) {human}")
    print(f"4) {orc}")
    print("5) Exit game?")
    character = input("Choose your character: ")
    character = character.casefold()
    print("")
    
    if character == "1" or character == "wizard":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    elif character == "2" or character == "elf":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    elif character == "3" or character == "human":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break
    elif character == "4" or character == "orc":
        character = orc
        my_hp = orc_hp
        my_damage = orc_damage
        break
    elif character =="5" or character == "exit":
        print("End game")
        exit()
    else:
        print("Unknown character")

print(f"You have chosen the character: {character}")
print(f"Health: {my_hp}")
print(f"Damage: {my_damage}")
print("")

# Battle with the dragon
while True:
    dragon_hp -= my_damage
    print(f"The {character} damaged the Dragon!")
    print(f"The Dragon's hitpoints are now: {dragon_hp}")
    print("")
    
    if dragon_hp <= 0:
        print("The Dragon has lost the battle")
        break

    my_hp -= dragon_damage
    print(f"The Dragon strikes back at {character}")
    print(f"The {character}'s hitpoints are now: {my_hp}")
    print("")

    if my_hp <= 0:
        print(f"{character} has lost the battle")
        break