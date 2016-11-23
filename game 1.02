import time

health = 10
inventory = ['clothes']
player_name = raw_input("What is your name? > ")

"""world items"""
topdrawer_items = 'full'
bottomdrawer_items = 'full'


"""Statements about stuff"""
topdraweritem_statement = "You take the health potion"
bottomdrawer_statement = "You take the rusty iron knife"


"""World Descriptions"""

#Bridge
bridge = "%s is on a bridge looking out over a small brook. In the distance there is the broken windmill of an abandonded farmhouse" % player_name
underbridge = "Under the bridge is dark with thick, wet moss growing through the cobble cracks, dripping like living green stalactites as they hang from the damp stone ceiling. You see a small door under the bridge, the cracks around the edges illuminated by a thin light causing dancing shadows to play across the rippling brook water"
roomunderbridge = "A small six foot by six foot alcove illumintated by a single flickering torch is revealed as the door is opened. Within is a small wooden dresser with two drawers, a top drawer and a bottom drawer. The dresser looks old." 
topdrawer = "You find a healing potion. It glows with inner light."
bottomdrawer = "The drawer bottom crumbles from decay as it is opened. A rusty iron knife clatters to the ground."


#Windmill
windmill = "%s is at the broken windmill. The structure has a wooden door adjar and swinging in the gentle breeze. The wooden windmill blades have rotted and fallen off long ago" % player_name
windmillfloor = "%s walks in and sees a stone spiral staircase winding around the outside of the room to the second floor. In the middle is a glass chandelier hanging crookedly on the ceiling. In the right corner there is a crushed desk laying on the ground. On the left corner is a small door." % player_name
windmillstairup = "You climb the staircase."
windmillstairdown = "You decend the staircase."
windmillfloor2 = "The second floor is a large open room that has a large device that looks like it was used to grind flour. On one wall there is a small staircase that goes to the third floor. Behind is a stair down. A giant mural of the windmill is on the opposite wall."
windmillfloor3 = "The third floor is a another large open room that has many boxes and bags. It appears to be a storage room. In the left corner is a small door like the one on the first floor."
windmillsecretdoor1 = "The room is a small square tower going all the way up to the third floor. On one wall there is a small platform that appears to be able to hoist you up to the top floor. On all the other walls there are pegs with rope tied in a circle around the room. All the pegs appear empty except the three at the top which you cannnot see"
windmillsecretdoor2 = "You are on a small platfrom. Next to you is the elevator shaft that you saw on the first floor. The three hooks you saw have decaying bodies hanging with ropes around their necks. The smell is horrifying"

print "Your name is %s" % player_name
print "/n"
print "Type 'inventory' to see the inventory \nType HP to see health \n"

restart = True
while restart:
    restart = True
    location = bridge
    print location
    print "\n"
    action1 = 'none'
    action1 = raw_input("What do you do? > ")
    if action1 == 'inventory':
        print inventory
        continue
    if action1 == 'health':
        print "%s's health is %s" % (player_name, str(health))
        continue
    while action1 == 'suicide':
        health = 0
        print "%s's health is %s" % (player_name, str(health))
        restart = False
        continue
    while "windmill" in action1:
        location = windmill
        print location
        action2 = 'none'
        action2 = raw_input("What do you do? > ")
        while action2 == 'inventory':
            print inventory
            continue
        while action2 == 'health':
            print health
            continue
        while action2 == 'suicide':
            health = 0
            continue
        while "bridge" in action2:
            break
        while "inside" or "door" or "open" in action2:
            location = windmillfloor
            print location
            action3 = 'none'
            action3 = raw_input("What do you do? > ")
            if action3 == 'inventory':
                print inventory
                continue
            if action3 == 'health':
                print health
                continue
            if "outside" in action3:
                break
            while "up" in action3:
                location = windmillfloor2
                print location
                action4 = 'none'
                action4 = raw_input("What do you do? > ")
                if action4 == 'inventory':
                    print inventory
                    continue
                if action4 == 'health':
                    print health
                    continue
                if "down" in action4:
                    print windmillstairdown
                    break
                while "up" in action4:
                    location = windmillfloor3
                    print location
                    action5 = raw_input("What do you do? > ")
                    if action5 == 'inventory':
                        print inventory
                        continue
                    if action5 == 'health':
                        print health
                        continue    
                    if "down" in action5:
                        print windmillstairdown
                        break
            while "door" in action3:
                location = windmillsecretdoor1
                print location
                action4 = 'none'
                action4 = raw_input("What do you do? > ")
                if action4 == 'health':
                    print health
                    continue
                if action4 == 'inventory':
                    print inventory
                    continue
                if "out" in "hoist" or "activate" in action4:
                    location = windmillsecretdoor2
                    print location
                    action5 = 'none'
                    action5 = raw_input("What do you do? > ")
                    if action5 == 'inventory':
                        print inventory
                        continue
                    if action5 == 'health':
                        print health
                        continue
                    while "suicide" or "jump" in action5:
                        print "You have joined the hanging corpses. You watch as your dim view of the world around you turns blurry and slowly fades to black"
                        time.sleep(10)
                    if "down" in action5:
                        print "You may not go down"
                        continue
    while "under bridge" or "below bridge" in action1:
        location = underbridge
        print location
        action2 = 'none'
        action2 = raw_input("What do you do? > ")
        if action2 == 'inventory':
            print inventory
            continue
        if action2 == 'health':
            print health
            continue    
        if "leave" in action2:
            break
        while "inside" or "door" in action2:
            location = roomunderbridge
            print location
            action3 = 'blank'
            action3 = raw_input("What do you do? > ")
            if action3 == 'inventory':
                print inventory
                continue
            if action3 == 'health':
                print health
                continue    
            if "leave" in action3:
                break
            while "top" in action3:
                sees = topdrawer
                print sees
                action4 = 'blank'
                action4 = raw_input("What do you do? > ")
                if action4 == 'inventory':
                    print inventory
                    continue
                if action4 == 'health':
                    print health
                    continue    
                while "take" or "pick up" in action4:
                    if topdrawer_items != 'empty':
                        inventory += ['health potion']
                    print inventory
                    print topdraweritem_statement
                    topdraweritem_statement = "Nothing to take."
                    topdrawer = "The top drawer is empty now."
                    topdrawer_items = 'empty'
                    print ""
                    break
                break
            while "bottom" in action3:
                sees = bottomdrawer
                print sees
                action4 = 'blank'
                action4 = raw_input("What do you do? > ")
                if action4 == 'inventory':
                    print inventory
                    continue
                if action4 == 'health':
                    print health
                    continue    
                while "take" or "pick up" in action4:
                    if bottomdrawer_items != 'empty':
                        inventory += ['knife']
                    print inventory
                    print bottomdrawer_statement
                    bottomdrawer_statement = "There is nothing to take."
                    bottomdrawer = "The bottom drawer is empty and looks like the broken bottom could not possible hold anything anymore."
                    bottomdrawer_items = 'empty'
                    print ""
                    break
                break
            continue
        continue
    continue
