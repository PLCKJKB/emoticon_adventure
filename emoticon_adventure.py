# Emoticon Adventure

import random
from itertools import zip_longest
import time
from pick import pick


name = ""

location = "start"

inventory = []

enchantments = []

friends = []

health = 100 

maxhealth = 100

gold = 0

permissions = [] 

def say(text,talker): #function for stylized talking bubbles

    lines = text.splitlines()
    talker_lines = talker.splitlines()
    print(" " * (len(max(talker_lines, key = len)) + 1),"~" * (len(max(lines, key = len)) + 4))
    for i, (line,talker_line) in enumerate(zip_longest(lines,talker_lines,fillvalue="")):
        if i == 0:
            print(f"{talker_line}"," " * (len(max(talker_lines, key=len))-len(talker_line)),">",f"{line}")
        else:
            print(f"{talker_line}"," " * (len(max(talker_lines, key=len))-len(talker_line))," ",f"{line}")
    print(" " * (len(max(talker_lines, key = len)) + 1),"~" * (len(max(lines, key = len)) + 4))



def valid_output(question,options):
    answer, index = pick(options,question,"-->")
    return(index+1)

# End function

def defeat():
    global  enchantments, inventory, friends, name, gold, maxhealth, health
    print("You perished! But you did well.")
    endgame(input(""))
    print("In your inventory you had:")
    for i in inventory:
        print(i)
    endgame(input(""))
    print("And you had these enchantments:")
    for i in enchantments:
        print(i)
    endgame(input(""))
    choice = valid_output(
        "Try again?",
        ["Yes","No"]
    )
    if choice == 1:
        print("Restarting...")
        enchantments = []
        inventory = []
        friends = []
        maxhealth = 100
        health = maxhealth
        gold = 0
        name = ""
        start_adventure()
    elif choice == 2:
        print("Goodbye!")
        quit()
    

#Travel variables

visited = []

# DESTINATION FUNCTIONS

def tutors_lair():
    global gold, health,maxhealth
    print("The castle looms over you. Through the windows you see various sillhoutes moving and mingling around. \nSome windows glow green, some red, some pure white.")
    endgame(input(""))
    if ";]" in friends or ";]healed" in friends:
        say("So this is where that bastard has been hiding this entire time. He'll pay... ",">;[")
        endgame(input(""))
        say(f"O-Of course this is your 'revenge' quest {name}, don't let my emotions get in your way.",");[")
        endgame(input(""))
    print("The castle has 5 floors. At the top is the tutor.")
    endgame(input(""))
    print("You slip inside through the door. You are in the entrance hall of the castle.\nNot a soul is around. You start exploring.")
    endgame(input(""))
    floor = 1
    while floor != 6:
        if floor == 1:
            result = valid_output(
                "Connecting to the entrance hall are doors connecting from the left and right. Which one do you go through?",
                ["Left","Right"]
            )
            if result == 1:
                print("You freeze the moment you enter. An Emoticon beast, \njust like the one you saw in the dungeon is standing right in front of you.")
                endgame(input(""))
                say("You shall pewish in the name of the tutor!",">:D")
                result = fight(20,3,1,1,2)
                if result == "defeat":
                    defeat()
                    return
                print("From the dust of the beast, coins roll out. It seems that these domesticated beasts carry around money.")
                goldgained =  random.randint(1,5)
                gold += goldgained
                endgame(input(""))
                print("You walk to the next door.")
                
            elif result == 2:
                print("You freeze the moment you enter. An Emoticon beast, \njust like the one you saw in the dungeon is standing right in front of you. \nBut this one seems stronger.")
                endgame(input(""))
                say("You shall pewish in the name of the tutor!",">:D")
                result = fight(30,5,2,1,3)
                if result == "defeat":
                    defeat()
                    return
                print("From the dust of the beast, coins roll out. It seems that these domesticated beasts carry around money.")
                goldgained =  random.randint(5,10)
                gold += goldgained
                endgame(input(""))
                print("You walk to the next door.")
                
            endgame(input(""))
            print("You open the door and see a library full of books. Some glow with power. Some with wisdom. Some... just don't glow.")
            endgame(input(""))
            choice = valid_output(
                "What book do you take with?",
                ["A book glowing with power","A book glowing with wisdom","A book"]
            )
            if choice == 1:
                print("The book is titled 'How to battle a titan'.")
                endgame(input(""))
                print("You now deal 1.5 times more damage to enemies above 20 HP!")
                enchantments.append("Titan")
            elif choice == 2:
                print("The book is titled 'The art of precision'.")
                endgame(input(""))
                print("You are now more likely to hit a crit!")
                enchantments.append("Precise Blade")
            elif choice == 3:
                print("The book is titled 'The Very Thick Book For Defense'.")
                endgame(input(""))    
                print("Your defense action improves!")
                inventory.append("Thick Book")
            
            endgame(input(""))
            print("You emerge from the library door.")
            endgame(input(""))
            print("The stairs glow with green light. You feel rejuvanated as you ascend to the next floor.")
            endgame(input(""))
            health = min(health + 10,maxhealth)
            floor += 1

        elif floor == 2:
            print("The stairs lead you to a sparkling hall, with quartz pillars lemming the sides.\nThere are four doors branching from it.")
            endgame(input(""))
            result = valid_output(
                "Which door do you pick?",
                ["Wooden door","Metal door","Mirror door","Gold door"]
            )
            if result == 1:
                print("The wooden door leads to a beautiful garden. In the middle, a large oak stands. Makes you wonder how it fits. \nFrom the tree leads a tube drawing sap from the tree.")
                endgame(input(""))
                if ";]" in friends:
                    say("This oak must have some sort of healing effect. Why else would the tutor extract its sap? I say we taste some sap!",";]")
                    endgame(input(""))
                elif ";]healed" in friends:
                    say("This oak must have some sort of healing effect. Why else would the tutor extract its sap?",";]")
                    endgame(input(""))
                else:
                    print("You decide to taste some sap.")
                    endgame(input(""))
                
                maxhealth += 50
                print("Your max health increased by 50!")

                if ";]" in friends:
                    endgame(input(""))
                    say("Wow! I feel amazing! I can walk again!",";]")
                    friends.remove(";]")
                    friends.append(";]healed")
                
            elif result == 2:
                print("The metal door leads you to an abandoned training room. \nBooks and rusty swords lay scattered around the room. \nYou pick up a book. It's titled 'Parrying for beginners'. Again, you seem to absorb the knowledge instantly.")
                endgame(input(""))
                print("Obtained 'Parrying Stance'! Now, a succesful defense, buffs your next attack.")
                enchantments.append("Parrying Stance")

            elif result == 3:
                print("The mirror door leads you to a room filled with mirrors. In the middle is a radiating light beam. Stepping into it fills your head with knowledge.")
                endgame(input(""))
                print("You've learned 'Reflective Guard'! Now, 50 percent of damage you block gets reflected back at the enemy! But it cannot kill it!")
                enchantments.append("Reflective Guard")

            elif result == 4:
                print("The gold door leads you to an empty room with a golden pedastal in the middle. On it lays a rune. You slap it onto your sword.")
                endgame(input(""))
                print("Obtained 'Greedy Rune'! Every bullseye you land gives you some coins!")
                enchantments.append("Greedy Rune")

            endgame(input(""))
            print("The room exits to a long hallway. At one side its a dead end, on the other it opens up to a wide space")
            endgame(input(""))
            print("You walk into the open room. There an armored Emoticon stands guard.")
            endgame(input(""))
            say("Hey! What are you doing here?! You're not allowed to be here!","_____\n|\ /|\n|O O|\n|/¯\|\n¯¯¯¯¯")
            result = fight(50,10,3,1,3)
            if result == "defeat":
                defeat()
                return
            print("You gain 50 coins from the guard, and you go to the next floor, healing 10 health")
            gold += 50
            health = min(health+10,maxhealth)
            floor += 1

        elif floor == 3:
            endgame(input(""))
            print("As you emerge from the stairs, a voice calls to you:")
            say("Psst! Hey kid! Want to buy something? I got anything you need, for a price...",".3-")
            endgame(input(""))
            while True:
                result = valid_output(
                    f"What do you want to buy? You have {gold} gold.",
                    ["Glass Cannon [20 gold]","Even Steven [20 gold]","Momentum [20 gold]","Snack [5 gold]","Nothing"]
                )
                if result == 1:
                    if gold < 20:
                        say("You can't afford that!","\ /\n.3.")
                        endgame(input(""))
                        continue
                    if "Glass Cannon" in enchantments:
                        say("You already bought this! Screw off!","\ /\n-3-")
                        endgame(input(""))
                        continue
                    print("This multiplies the damage you deal by 3, but also multiplies the damage you can take by 3.")
                    endgame(input(""))

                    choice = valid_output(
                        "Do you want to buy this enchantment?",
                        ["Yes","No"]
                    )

                    if choice == 1:
                        say("Pleasure doing business with ya!","^3^")
                        endgame(input(""))
                        gold -= 20
                        enchantments.append("Glass Cannon")

                elif result == 2:
                    if gold < 20:
                        say("You can't afford that!","\ /\n.3.")
                        endgame(input(""))
                        continue
                    if "Even Steven" in enchantments:
                        say("You already bought this! Screw off!","\ /\n-3-")
                        endgame(input(""))
                        continue
                    print("This makes your damage times 2, if your health is an even number.")
                    endgame(input(""))

                    choice = valid_output(
                        "Do you want to buy this enchantment?",
                        ["Yes","No"]
                    )

                    if choice == 1:
                        say("Pleasure doing business with ya!","^3^")
                        endgame(input(""))
                        gold -= 20
                        enchantments.append("Even Steven")

                elif result == 3:
                    if gold < 20:
                        say("You can't afford that!","\ /\n.3.")
                        endgame(input(""))
                        continue
                    if "Momentum" in enchantments:
                        say("You already bought this! Screw off!","\ /\n-3-")
                        endgame(input(""))
                        continue

                    print("If your last attack was a bullseye, your next attack will be boosted!")
                    endgame(input(""))

                    choice = valid_output(
                        "Do you want to buy this enchantment?",
                        ["Yes","No"]
                    )

                    if choice == 1:
                        say("Pleasure doing business with ya!","^3^")
                        endgame(input(""))
                        gold -= 20
                        enchantments.append("Momentum")
                    
                elif result == 4:
                    if gold < 5:
                        say("You can't afford that!","\ /\n.3.")
                        endgame(input(""))
                        continue

                    print(f"This scrumptious snack heals you 15 health. Remind you, your current health is {health}/{maxhealth}")
                    endgame(input(""))

                    choice = valid_output(
                        "Do you want to buy this snack?",
                        ["Yes","No"]
                    )

                    if choice == 1:
                        say("Pleasure doing business with ya!","^3^")
                        endgame(input(""))
                        gold -= 5
                        health = min(health + 15, maxhealth)

                elif result == 5:
                    say("Thanks for browsing!",".3.")
                    break

            endgame(input(""))
            print("As the merchant scuffles away, you finally look around the room.")
            endgame(input(""))
            print("It is an alchemy lab. Bubbling liquids flow everywhere around you.")
            endgame(input(""))
            print("Before you are 3 flasks: A red one, a green one and a blue one.")
            endgame(input(""))

            result = valid_output(
                "Which one do you drink?",
                ["The red one.","The green one.","The blue one."]
            )
            
            if result == 1:
                print("Your strength increases, you now deal 1 more base damage!")
                enchantments.append("Strength")
            elif result == 2:
                print("You feel rejuvenated. You heal to max health!")
                health = maxhealth
            elif result == 3:
                print("Your skin feels tougher. You take less damage!")
                enchantments.append("Stone Skin")

            endgame(input(""))
            say("Hey! What are you doing out here? I thought I put you in jail!","(8[")
            endgame(input(""))
            say("Nevermind! I'll stop you with my latest concotion!",">8]")
            endgame(input(""))
            say("MUHAHAHAHAHA I FEEL THE POWERRRRR!","\  /\nO><O\n\__/")
            endgame(input(""))
            print("The tutors silhoutte crashes through the ceiling.")
            endgame(input(""))
            say("Uhhh...","_\nO><O\n____")
            endgame(input(""))
            say("I can't see you... guess I'll just stomp you?","O><O\n____")
            endgame(input(""))
            print("BOSSFIGHT: FIRST PHASE: Tutor's legs")
            endgame(input(""))
            result = fight(100,10,5,1,3,"swift")
            if result == "defeat":
                defeat()
                return

            say("Ow! My legs! Come up here and fight me like a man! Or woman. I don't care what your pronouns are.","\  /\nO><O\n/¯¯\ ")
            endgame(input(""))
            print("From underneath the tutors foot, a red bottle falls out. You drink it. \n\nYou gained Vampiric Drain! Now you heal from your attacks.\nYou also find a pouch of 75 coins.")
            enchantments.append("Vampiric Drain")
            gold += 75
            endgame(input(""))
            print(f"Gold: {gold}")
            endgame(input(""))
            print("As you go to the next floor, you heal 10 hp.")
            health = min(health+10,maxhealth)
            
            floor += 1
        
        elif floor == 4:
            endgame(input(""))
            say("What did you do down there?!","_ -\n.3.")
            endgame(input(""))
            say("Ah, nevermind. I see you have new cash, and my stocks restocked. Want a peak?","-3-")
            while True:
                result = valid_output(
                    f"What do you want to buy? You have {gold} gold.",
                    ["Midas Touch [30 gold]","Perseverance [30 gold]","Desperation [30 gold]","Exquisite Snack [10 gold]","Nothing"]
                )

                if result ==  1:
                    if gold < 30:
                        say("You can't afford that!","\ /\n.3.")
                        endgame(input(""))
                        continue
                    if "Midas Touch" in enchantments:
                        say("You already bought this! Screw off!","\ /\n-3-")
                        endgame(input(""))
                        continue

                    print("The more gold you own, the more damage you deal!")
                    endgame(input(""))

                    choice = valid_output(
                        "Do you want to buy this enchantment?",
                        ["Yes","No"]
                    )

                    if choice == 1:
                        say("Pleasure doing business with ya!","^3^")
                        endgame(input(""))
                        gold -= 30
                        enchantments.append("Midas Touch")

                elif result == 2:
                    if gold < 30:
                        say("You can't afford that!","\ /\n.3.")
                        endgame(input(""))
                        continue
                    if "Perseverance" in enchantments:
                        say("You already bought this! Screw off!","\ /\n-3-")
                        endgame(input(""))
                        continue

                    print("The longer the fight goes on, the more damage you deal! (You gain more damage per enemy attack.)")
                    endgame(input(""))

                    choice = valid_output(
                        "Do you want to buy this enchantment?",
                        ["Yes","No"]
                    )

                    if choice == 1:
                        say("Pleasure doing business with ya!","^3^")
                        endgame(input(""))
                        gold -= 30
                        enchantments.append("Perseverance")

                elif result == 3:
                    if gold < 30:
                        say("You can't afford that!","\ /\n.3.")
                        endgame(input(""))
                        continue
                    if "Desperation" in enchantments:
                        say("You already bought this! Screw off!","\ /\n-3-")
                        endgame(input(""))
                        continue

                    print("The less health you have, the more damage you deal!")
                    endgame(input(""))

                    choice = valid_output(
                        "Do you want to buy this enchantment?",
                        ["Yes","No"]
                    )

                    if choice == 1:
                        say("Pleasure doing business with ya!","^3^")
                        endgame(input(""))
                        gold -= 30
                        enchantments.append("Desperation")

                elif result == 4:
                    if gold < 10:
                        say("You can't afford that!","\ /\n.3.")
                        endgame(input(""))
                        continue

                    print(f"This ExQuIsItE snack heals you 40 health. Remind you, your current health is {health}/{maxhealth}")
                    endgame(input(""))

                    choice = valid_output(
                        "Do you want to buy this snack?",
                        ["Yes","No"]
                    )

                    if choice == 1:
                        say("Pleasure doing business with ya!","^3^")
                        endgame(input(""))
                        gold -= 10
                        health = min(health + 40, maxhealth)

                elif result == 5:
                    say("Thanks for browsing!",".3.")
                    break
            
            say("Well, that's the last you'll see of me. Im outta this joint.",".3-")
            endgame(input(""))
            say("Anyway, good luck with the tutor! If you win, I'll give you a hero's discount or something.","^3^")
            endgame(input(""))
            print("You both look to the door of the room as a rumble shakes the entire castle.")
            endgame(input(""))

            if ";]" in friends:
                say("Yep I'm out. And if you want, I can take your friend over here to safety as well.",".3.")
                endgame(input(""))
                say("I mean... sure? At least I won't get in the way.","/;[")
                friends.remove(";]")
                endgame(input(""))
            elif ";]healed" in friends:
                say("Yep I'm out. And if you want, I can take your friend over here to safety as well.",".3.")
                endgame(input(""))
                say("I mean... sure? At least I won't get in the way.","/;[")
                friends.remove(";]healed")
                endgame(input(""))
            else:
                say("Yep I'm out.","-3-")
                endgame(input(""))

            print("The tutors arm barges in through the wall, grabbing you and yanking you up to the last floor.")
            endgame(input(""))
            floor += 1

        elif floor == 5:
            say("Now I've got you! It's time we settle this. Get him my horde!","\  /\nO><O\n/¯¯\ ")
            print("BOSSFIGHT: SECOND PHASE: Tutor's horde")
            endgame(input(""))
            print("Four Emoticon Beasts attack you, they seem to be stronger then the other you've seen. But they have rejuvinating energy radiating from them. Defeating them all will surely heal you.")
            for i in range(4):
                result = fight(30, 4, 1, 1, 2,"chonky")
                if result == "defeat":
                    defeat()
                    return

            health = min(maxhealth,health*1.5)

            word = valid_output(
                "What do you say to the tutor?",
                ["You call that a horde?","Why are you so hellbent on doing whatever you want?","What's your deal with ;]?"]
            )

            if word == 1:
                say("4 is a lot! Shut up! I'm tired of your yapping. Let's end this. Now.","\  /\nO><O\n/¯¯\ ")

            elif word == 2:
                say("Because I've taught so many ding dongs like you, I just don't care what anyone thinks! \nAnd since you seemingly don't like what I do, you'll be the first to fall! And then I will... ","\  /\nO><O\n/¯¯\ ")
                endgame(input(""))
                say("Well probably not rule the world, that's a lot of responsibility...","O><O\n----")
                endgame(input(""))
                say("But I won't give a fluff on what anyone thinks about my actions!","\  /\nO><O\n\__/")

            elif word == 3:
                say("That grump? He didn't want to help me, so I locked him up. \nThat's it. \nI don't know what revenge quest he has but that's my side of the story.","O><O\n----")

            endgame(input(""))
            print("BOSSFIGHT: FINAL PHASE: The Tutor")
            result = fight(200,15,5,1,4,"berserk")
            if result == "defeat":
                defeat()
                return

            say("OH screw you! No one can have fun around here. -bleh-","-  -\nO><O\n----")
            endgame(input(""))
            print("And as the tutors body dissapates into dust, a chapter of your life closes behind you. \nYou look over the forest. You feel proud over what you've accomplished. But you feel more chapters ahead of you.")
            endgame(input(""))
            print("Chapter 1: COMPLETE")
            endgame(input(""))
            print("Thank you for playing Emoticon Adventure. I might make more, who knows.")
            floor += 1




            






def tutors_dungeon():
    global gold
    global health
    if not ("Tutors Dungeon" in visited):
        visited.append("Tutors Dungeon")
    print("You step out of the cell.")
    endgame(input(""))
    say("Wait!","(;[")
    endgame(input(""))
    say("I... I've been here way too long, I've gotten too weak to walk out by myself... \nCould you help me out maybe?",");[")
    endgame(input(""))
    result = valid_output(
        "Do you help ;[ ?",
        ["Yes","No"]
    )
    if result == 1:
        say("Thank you very much!",";]")
        friends.append(";]")
        endgame(input(""))
        print("You walk alongside ;], supporting his weight.")
        endgame(input(""))
    else:
        say("Aw man...",";[")
        endgame(input(""))
    print("As you walk down the corridor, a wild Emoticon Beast jumps out from the shadows.")
    endgame(input(""))
    say("You shall pewish!",">:3")
    endgame(input(""))
    if ";]" in friends:
        say("I might burden you in this battle a bit, but I promise I'll make up for it.\nBeasts like that tend to take a few hits, but they don't do much damage back.",";/")
    result = fight(20,3,1,1,2)
    if result == "defeat":
        defeat()
        return
    say("I have been vanquished",")X3")
    endgame(input(""))
    if ";]" in friends:
        say("Great job dealing with that Beast! We should hurry on onward before more arrive.",";]")
        endgame(input(""))
    result = valid_output(
        "You arrive at a fork in the hallway. \nFrom the left, a green light emanates, and a herbal smell wafts towards you.\nFrom the right, a red fiery glow emanates.\nWhere do you go?",
        ["Left","Right"]
    )
    if result == 1:
        visited.append("The Fountain")
        print("You come across a glowing fountain. The water flowing in it is a sparkly green.")
        if ";]" in friends:
            say("So this is how the tutor's been around for so long... \nThis fountain has to be vitality replenishing!","(;[")
            endgame(input(""))
            result = valid_output(
                "What do you do with the fountain?",
                ["Drink from it. [Heal 20 health]","Make a wish. [-1 gold, gain something in return?]","Let ;] drink from it. [Lose the BURDENED debuff]"]
            )
        else:
            result = valid_output(
                "What do you do with the fountain?",
                ["Drink from it. [Heal 20 health]","Make a wish. [-1 gold, gain something in return?]"]
            )
        if result == 1:
            print("You heal 20 health.")
            health =  min(health + 20, maxhealth)
            endgame(input(""))
        elif result == 2:
            print("You toss in a coin. The water starts fizzing after it hits the surface.\nA foaming hand rises from the water. It's holding a bracelet with a green gem imbeded in it\nIt grabs your arm, and slides it onto your wrist.")
            print("\nHealing Bracelet has been added to your inventory!\nHeal half of the damage you deal.")
            inventory.append("Healing Bracelet")
            print("Check your inventory!")
            gold -= 1
            do_action()
        elif result == 3:
            print("You lower ;] to the fountain.")
            say("You... you want me to drink? I appreciate that!","(;]")
            endgame(input(""))
            say("-slurp slurp- Wow! I feel much better! I feel I could walk for ages!","(;]")
            endgame(input(""))
            print("You are no longer burdened by ;]")
            friends.remove(";]")
            friends.append(";]healed")
    elif result == 2:
        visited.append("The Armory")
        print("You come across a firey pit of energy. In the middle of the pit, a red ruby glows bright as the sun. \nText on the edge says: 'The Fuel Of The Gods Armory'.")
        endgame(input(""))
        if ";]" in friends:
            say("This is where the tutor wanted me to work orignally\nbut after I refused that too, I ended up in the cell.","|;[")
            endgame(input(""))
            say("But it's a true beauty this place.\nI think if I tried real hard I could enhance that sword of yours.",";]")
            result = valid_output(
                "What do you do?",
                ["Throw your sword into the pit [Extra crit.]","Dip your sword into the fire [Upgrade Blazing Edge]","Let ;] upgrade your sword [???]"]
            )
        else:
            result = valid_output(
                "What do you do?",
                ["Throw your sword into the pit [Extra crit.]","Dip your sword into the fire [Upgrade Blazing Edge]"]
            )
        if result == 1:
            print("You throw your sword, the fire enveloping it whole. After a few seconds it flies out, it's edge glowing bright red.")
            endgame(input(""))
            print("Obtained the 'Deadly Bullseye' enchantment! All outcomes of the crits will do more damage.")
            enchantments.append("Deadly Bullseye")
            endgame(input(""))
        elif result == 2:
            print("You lower the blade into the fire. Immediatly your Blazing Edge reacts, burning hotter than ever.")
            endgame(input(""))
            print("Your 'Blazing Edge' enchantment has upgraded to 'Blazing Edge II'!")
            enchantments.remove("Blazing Edge")
            enchantments.append("Blazing Edge II")
            endgame(input(""))
        elif result == 3:
            say("Well, haven't done this in a long time, but here goes.",";]")
            endgame(input(""))
            print("You sit back, watching ;] swing a hammer across the sword in such a natural way, it makes it look like nothing.")
            endgame(input(""))
            say("Aaaaand...",";]")
            endgame(input(""))
            say(f"Done! Here you go {name}!",";]")
            endgame(input(""))
            print("The sword you hold feels unrecognizable. It's light as a feather, and it glimmers in a magical way.")
            endgame(input(""))
            print("Obtained ';] Sword'! With this sword, you're able to land 2 hits during fights!")
            inventory.remove("Sword")
            inventory.append(";] Sword")
            endgame(input(""))
    print("You reach the end of the hall. A huge oak door stands before you.")
    endgame(input(""))
    if ";]" in friends or ";]healed" in friends:
        print("Suddenly a huge shadow looms over you and ;]")
    else:
        print("Suddenly a huge shadow looms over you.")
    say("The tutor warned we might have\n a itty bitty jail break today!\n Not on my watch buckos!","\ /\nO O\n\_/")
    endgame(input(""))
    say(f"I will crush you into pieces! Come at me, {name}!","\ /\nO O\n___")
    result = fight(50,7,3,1,3)
    if result == "defeat":
        defeat()
        return

    say("Well, I guess you defeated me. Time to turn to dust. Bleh.","_ _\nX O\n___")
    endgame(input(""))
    print("From the pile of dust, two items peek out: \nA bottle of green liquid \nAnd a sharpening stone glowing red.")
    endgame(input(""))
    result = valid_output(
        "What do you take?",
        ["Green Bottle [Full Heal]","Sharpening Stone [+2 weapon damage]"]
    )
    if result == 1:
        print(f"You drink the liquid, and you feel amazing. \n Health: {maxhealth}/{maxhealth}.")
        endgame(input(""))
        health = maxhealth
    elif result == 2:
        print("You scrape the stone against your sword, and the edge becomes leagues sharper.")
        endgame(input(""))
        enchantments.append("Sharp Edge")

    if ";]" in friends or ";]healed" in friends:
        say("Great job! Now we can leave! And put an end to the tutors madness.",";]")
        endgame(input(""))

    print("You heave open the oak door.")
    endgame(input(""))
    print("Sunlight hits your face. You're outside. And before you stands a huge castle.")
    global lastlocation, location
    lastlocation = location
    location = "tutors_lair"
    tutors_lair()




def tutors_dungeon_cell():
    if not ("Tutors Dungeon Cell" in visited):
        visited.append("Tutors Dungeon Cell")
    print("You wake up in a cold cell.")
    endgame(input(""))
    say("You angered the tutor too huh?",";/")
    endgame(input(""))
    while True:
        if "Sword" in inventory:
            result = valid_output(
                "What do you do?",
                ["Explore the cell.","Talk to your cellmate","Call for help.","Try to break out with your sword."]
            )
        else:
            result = valid_output(
                "What do you do?",
                ["Explore the cell.","Talk to your cellmate","Call for help."]
            )
        if result == 1:
            if "Blazing Edge" in enchantments:
                print("You don't find anything significant.")
            else:
                print("As you stumble around in the dark, tracing the wall with your hand, \na stone slab gives away beneath your hand. \nInside you find a book titled 'The Art of The Blazing Edge' \nYou somehow instantly know how to use it. \nYou also find 2 gold.")
                endgame(input(""))
                print("Obtained the Blazing Edge enchantment!")
                enchantments.append("Blazing Edge")
                global gold
                gold += 2
                print(f"You now have {gold} gold!")

        elif result == 2:
            while True:
                result = valid_output(
                    "What do you ask?",
                    ["Why are you in here?","Who is the tutor?","Nothing."]
                )
                if result == 1:
                    say("I refused to lend him some equipment for his trainees. \nI used to be a blacksmith you know.\nWhen I get my hands on him...",">;|")
                    endgame(input(""))
                elif result == 2:
                    say("The tutor is some entitled bozo who thinks that because he teaches you something \nhe suddenly can do anything he wants.",">;|")
                    endgame(input(""))
                elif result == 3:
                    say("Okay then.",";]")
                    endgame(input(""))
                    break
        elif result == 3:
            print("Your call just echoes back to you...")
            endgame(input(""))
        elif result == 4:
            if "Blazing Edge" in enchantments:
                print("Your Blazing Sword cuts through the bars like butter.")
                endgame(input(""))
                global lastlocation, location
                lastlocation = location
                location = "tutors_dungeon"
                tutors_dungeon()
                return
            else:
                print("Your sword clangs pointlessly against the bars.")
                endgame(input(""))







def check_status(): #writes out player status
    print(f"Health: {health}/{maxhealth}")
    print("Inventory:")
    for item in inventory:
        print(item)


# Fight functions

def defend(hplost,lowerrangeofchance,upperrangeofchance):
    number = random.randint(int(lowerrangeofchance),int(upperrangeofchance))
    if "Thick Book" in inventory:
        number =  random.randint(int(lowerrangeofchance),min(int(upperrangeofchance)-1,2))
    while True:
        try:
            if "Thick Book" in inventory:
                print(f"To defend, try to guess the number,\n it's between {lowerrangeofchance} and {upperrangeofchance-1}.")
            else:
                print(f"To defend, try to guess the number,\n it's between {lowerrangeofchance} and {upperrangeofchance}.")
            answer = int(input("Try to guess the number:"))
            if answer == number:
                if "Thick Book" in inventory:
                    defended = random.randint(5,15)
                    reduced = max(0,hplost-defended)
                else:
                    defended = random.randint(1,10)
                    reduced = max(1,hplost-defended)
                print(f"You defended {hplost-reduced} out of {hplost} damage!")

                return  reduced, defended
            else:
                print("Your defending failed!")
                return  hplost, 0 
                
        except ValueError:
            print("Not a valid input.")

def dmgeffect(dmgdealt,mincritrange,maxcritrange):
    global gold
    number =  random.randint(int(mincritrange),int(maxcritrange))
    while True:
        try:
            print("Guess the number, the closer you get, the more powerful your attack!")
            answer = int(input(f"Guess, it's between {mincritrange} and {maxcritrange}:"))
            if answer == number:
                if "Deadly Bullseye" in enchantments:
                    dmgdealt = round(dmgdealt * 2.5,1)
                else:
                    dmgdealt = round(dmgdealt * 2.1,1)

                if "Greedy Rune" in enchantments:
                    goldgained = random.randint(1,5)
                    gold += goldgained
                    print(f"The Greedy Rune gives you {goldgained} gold!")

                crit = True

                print(f"Bullseye! You deal {dmgdealt} damage!")
            elif answer + 1 == number or answer - 1 == number:
                crit = False
                if "Deadly Bullseye" in enchantments:
                    dmgdealt = round(dmgdealt * 2.1,1)
                else:
                    dmgdealt = round(dmgdealt * 1.7,1)
                
                print(f"Close! You deal {dmgdealt} damage!")
            elif answer + 2 == number or answer - 2 == number:
                crit = False
                if "Deadly Bullseye" in enchantments:
                    dmgdealt = round(dmgdealt * 1.7,1)
                else:
                    dmgdealt = round(dmgdealt * 1.3,1)
                print(f"Almost there! You deal {dmgdealt} damage!")
            elif answer + 3 == number or answer - 3 == number or answer + 4 == number or answer - 4 == number:
                crit = False
                dmgdealt = round(dmgdealt * 1,1)
                print(f"You don't crit. You deal {dmgdealt} damage!")
            else:
                crit = False
                dmgdealt = round(dmgdealt * 0.8,1)
                print(f"Oh, you failed bad! You deal {dmgdealt} damage!")
            return round(dmgdealt,1), crit

        except ValueError:
            print("Not a valid input.")

def fight(enemyhp,maxenemydmg,minenemydmg,defenddownvalue,defendupvalue,trait= "none"):
    global health, gold, maxhealth
    endfight = False
    bullseye = False
    maxenemyhp = enemyhp
    defended = 0
    strikes = 1
    fightlength = 0
    NextTurn = False
    if ";]" in friends:
        burdened = True
    else:
        burdened = False
    print("Starting fight...")
    endgame(input(""))
    print("You're attacking...")
    endgame(input(""))
    while endfight == False:
        if "Sword" in inventory:
            dmg = 3
            strikes = 1
            upcrit = 10

        elif ";] Sword" in inventory:
            dmg = 3
            strikes = 2
            upcrit = 10    

        elif "weapon" in inventory:
            pass #other weapons

        else:
            print("You don't have a weapon to fight with.")
            hplost = random.randint(minenemydmg,maxenemydmg)
            health -= hplost
            endgame(input(""))
            print(f"You took {hplost} damage!")
            print(f"HP: {health}/{maxhealth}")
            endfight = True
            dmgdealt = 0

        if "Strength" in enchantments:
            dmg += 1
        
        if "Sharp Edge" in enchantments:
            dmg += 2

        if "Precise Blade" in enchantments:
            upcrit -= 2

        for strike in range(strikes):
            if enemyhp > 0:
                if strike >= 1:
                    print("The swiftness of your sword allows another strike.")
                    dmgdealt, bullseye = dmgeffect(dmg, 0, upcrit)
                else:
                    dmgdealt, bullseye = dmgeffect(dmg, 0, upcrit)

                if burdened:
                    dmgdealt = round((dmgdealt * 0.9),1)
                    print(f"You are burdened, your damage decreased to {round(dmgdealt,1)}")
                    endgame(input(""))

                if "Blazing Edge" in enchantments:
                    dmgdealt = round((dmgdealt * 1.2),1)
                    print(f"Your Blazing Edge increases your damage to {round(dmgdealt,1)}")
                    endgame(input(""))

                if "Blazing Edge II" in enchantments:
                    dmgdealt = round((dmgdealt * 1.5),1)
                    print(f"Your Blazing Edge II increases your damage to {round(dmgdealt,1)}")
                    endgame(input(""))

                if "Titan" in enchantments and enemyhp >= 20:
                    dmgdealt = round(dmgdealt * 1.5,1)
                    print(f"Your Titan knowledge increases your damage to {dmgdealt}!")
                    endgame(input(""))

                if "Parrying Stance" in enchantments and defended > 0:
                    dmgdealt = round(dmgdealt * 2,1)
                    print(f"Your Parrying Stance makes your strike more powerful, boosting it to {dmgdealt}!")
                    endgame(input(""))

                if "Even Steven" in enchantments and health % 2 == 0:
                    dmgdealt = round(dmgdealt * 2,1)
                    print(f"You are an Even Steven. Your damage doubles to {dmgdealt}.")
                    endgame(input(""))

                if "Glass Cannon" in enchantments:
                    dmgdealt = round(dmgdealt * 3,1)
                    print(f"Your brittle spirit raises your damage to {dmgdealt}!")
                    endgame(input(""))

                if "Momentum" in enchantments and NextTurn == True:
                    dmgdealt = round(dmgdealt * (random.randint(15,25) / 10),1)
                    print(f"Your momentum boosts your attack to {dmgdealt}!")
                    NextTurn = False
                    endgame(input(""))

                if "Midas Touch" in enchantments:
                    mult =  (gold / 100) + 1
                    dmgdealt = round(dmgdealt * mult,1)
                    print(f"Your wealth increases your damage to {dmgdealt}!")
                    endgame(input(""))

                if "Perseverance" in enchantments:
                    mult = (fightlength / 10) + 1
                    dmgdealt = round(dmgdealt * mult,1)
                    print(f"Your perseverance increases your damage to {dmgdealt}!")
                    endgame(input(""))

                if "Desperation" in enchantments:
                    mult = ((maxhealth - health) / maxhealth) + 1
                    dmgdealt = round(dmgdealt * mult,1)
                    if mult != 1:
                        print(f"Your desperation increases your damage to {dmgdealt} damage!")
                        endgame(input(""))

                if "Healing Bracelet" in inventory:
                    healed = round(dmgdealt / 2,0)
                    health = min(health + healed,maxhealth)
                    print(f"The Healing Bracelet healed you {healed} health!")
                    print(f"Health: {health}/{maxhealth}")
                    endgame(input(""))

                if "Vampiric Drain" in enchantments:
                    healed = round(dmgdealt * 0.25)
                    health = min(health + healed,maxhealth)
                    print(f"Your Vampiric Drain healed you {healed} health!")
                    print(f"Health: {health}/{maxhealth}")
                    endgame(input(""))


                if endfight:
                    print("You dont have a weapon, you didnt deal damage!")
                    endgame(input(""))

                if trait == "chonky":
                    dmgdealt = round(dmgdealt * 0.75,1)
                    print(f"Your enemy's 'chunky' trait makes it take {dmgdealt} damage!")

                enemyhp = round(enemyhp - dmgdealt,1)
                print(f"Enemy health: {max(enemyhp,0)}/{maxenemyhp}")

                endgame(input(""))

            if bullseye == True:
                NextTurn = True

        if trait == "swift":
            enemyattacks = 2
        else:
            enemyattacks = 1


        for attack in range(enemyattacks):
            if enemyhp > 0:
                if attack == 1:
                    print("The enemy is swift, and is attacking again!")
                else:
                    print("The enemy is attacking...")

                endgame(input(""))

                hplost = random.randint(minenemydmg,maxenemydmg)
                
                if trait == "berserk":
                    mult = ((maxenemyhp - enemyhp)/ maxenemyhp) + 1
                    hplost = round(hplost * mult)
                    print(f"The enemy has gone berserk, increasing its damage to {hplost}")

                if "Glass Cannon" in enchantments:
                    hplost *= 3
                    print("Your brittle spirit will take more damage.")
                    endgame(input(""))

                hplost, defended = defend(hplost,defenddownvalue,defendupvalue)

                if "Reflective Guard" in enchantments and defended > 0:
                    print(f"Your Reflective Guard reflects {defended // 2} damage!")
                    enemyhp = round(max(enemyhp - (defended // 2),1),1)
                    print(f"Enemy health: {max(enemyhp,1)}/{maxenemyhp}")

                if "Stone Skin" in enchantments:
                    hplost = max(round(hplost * 0.8),0)
                    print(f"Your tough skin blocks the attack, reducing it to {hplost}!")

                health -= hplost

                fightlength += 1

                print(f"You took {hplost} damage!")
                endgame(input(""))
                print(f"HP: {max(health,0)}/{maxhealth}")
            if health <= 0:
                print("You were defeated.")
                return("defeat")
            print("\nYour turn to attack.")
        if enemyhp <= 0:
            print("The enemy is defeated.")
            return("victory")
            

    print("Come back stronger and with a weapon.")

def endgame(input):         
    if input == "exit":
        quit()

        
def do_action():
    action = input("Action:").strip().lower()
    while action != "pass":
        if action == "status":
            check_status()
        elif action == "exit":
            quit()
        else:
            print("Invalid action. Try again.")
        action = input("Action:").strip().lower()


def start_adventure():
    global location
    global name
    location = "start"

    print("Hello! Before you start playing, you should know some things: \nDO NOT HOLD ENTER, just lightly tap it to progress dialog, holding it could ruin the gameplay.\nThese lines you can write in are dialogue windows, pressing enter will progress you to the next dialogue.\nTry it now!")
    endgame(input(""))
    print("Now do it like that the rest of your playing, and enjoy the game!")
    endgame(input(""))

    say("Hi! I'm 8]. I'll be your tutor!","8]")
    endgame(input(""))
    say("Let's start simple. What's your name?","8]")
    name = input("Enter name:")
    say(f"{name} huh? Nice name!","(8]")
    endgame(input(""))
    say("Your goal for this tutorial will be to defeat this fierce creature:","8]")
    endgame(input(""))
    say("rawr",">:]")
    endgame(input(""))
    say("What a fierce creature.","8]")
    endgame(input(""))
    say("Anyway, to defeat it, you'll need a weapon. Here, have this sword.","8]")
    inventory.append("Sword")
    print("You obtained SWORD! \nSword does 3 dmg, with occasional crits.")
    endgame(input(""))
    say("When given the chance, you can type 'status' into the input window, \nand you'll see your items, and your health. Try it now! \nTo exit the action, just type 'pass'","8]")
    do_action()
    say("Ready to fight?","8]")
    endgame(input(""))
    say("You can also reduce the damge you take with a game of chance...","8]")
    endgame(input(""))
    result = fight(15,5,1,1,3)
    if result == "victory":
        say("sad rawr \nI is ded.",">X[")
        endgame(input(""))
        say("Great job! Let me heal you back up so we can continue.","8]")
        endgame(input(""))
        global health
        health = 100
        print("Your health returned to 100")
        endgame(input(""))
    elif result == "defeat": #even though its impossible, it makes a good failsafe
        say("Bruh. No way you died on the tutorial.","8[")
        defeat()

    say("So, what did you think of the tutorial?","8]")
    endgame(input(""))
    answer = valid_output(
        "What do you answer.",
        ["Boring.","Stupid.","Meh.","You're not good at this."]
    )
    say("What?!",">8[")
    endgame(input(""))
    say("Even though I should respect your opinion.",">8[")
    endgame(input(""))
    say("I won't. To the dungeon with you!","8]")
    location = "tutors_dungeon_cell"
    tutors_dungeon_cell()
    return


start_adventure()



