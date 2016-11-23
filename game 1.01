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
    action = raw_input("What do you do? > ")
    if action == 'inventory':
        print inventory
        continue
    if action == 'health':
        print "%s's health is %s" % (player_name, str(health))
        continue
    while action == 'suicide':
        health = 0
        print "%s's health is %s" % (player_name, str(health))
        restart = False
        continue
    while "windmill" in action:
        location = windmill
        print location
        action = raw_input("What do you do? > ")
        while action == 'inventory':
            print inventory
            continue
        while action == 'health':
            print health
            continue
        while action == 'suicide':
            health = 0
            continue
        while "bridge" in action:
            break
        while "inside" or "door" in action:
            location = windmillfloor
            print location
            action = raw_input("What do you do? > ")
            if action == 'inventory':
                print inventory
                continue
            if action == 'health':
                print health
                continue
            if "outside" in action:
                break
            while "up" in action:
                location = windmillfloor2
                print location
                action = raw_input("What do you do? > ")
                if action == 'inventory':
                    print inventory
                    continue
                if action == 'health':
                    print health
                    continue
                if "down" in action:
                    print windmillstairdown
                    break
                while "up" in action:
                    location = windmillfloor3
                    print location
                    action = raw_input("What do you do? > ")
                    if action == 'inventory':
                        print inventory
                        continue
                    if action == 'health':
                        print health
                        continue    
                    if "down" in action:
                        print windmillstairdown
                        break
            while "door" in action:
                location = windmillsecretdoor1
                print location
                action = raw_input("What do you do? > ")
                if action == 'health':
                    print health
                    continue
                if action == 'inventory':
                    print inventory
                    continue
                if "out" in action:
                    print "You go out"
                    break
                while "hoist" or "activate" in action:
                    location = windmillsecretdoor2
                    print location
                    action = raw_input("What do you do? > ")
                    if action == 'inventory':
                        print inventory
                        continue
                    if action == 'health':
                        print health
                        continue
                    while "suicide" or "jump" in action:
                        print "You have joined the hanging corpses. You watch as your dim view of the world around you turns blurry and slowly fades to black"
                        time.sleep(10)
                    if "down" in action:
                        print "You may not go down"
                        continue
    while "under bridge" or "below bridge" in action:
        location = underbridge
        print location
        action = raw_input("What do you do? > ")
        if action == 'inventory':
            print inventory
            continue
        if action == 'health':
            print health
            continue    
        if "leave" in action:
            break
        while "inside" or "door" in action:
            location = roomunderbridge
            print location
            action = raw_input("What do you do? > ")
            if action == 'inventory':
                print inventory
                continue
            if action == 'health':
                print health
                continue    
            if "leave" in action:
                break
            while "top" in action:
                sees = topdrawer
                print sees
                action = raw_input("What do you do? > ")
                if action == 'inventory':
                    print inventory
                    continue
                if action == 'health':
                    print health
                    continue    
                while "take" or "pick up" in action:
                    if topdrawer_items != 'empty':
                        inventory += ['health potion']
                    print inventory
                    print topdraweritem_statement
                    topdraweritem_statement = "Nothing to take."
                    topdrawer = "The top drawer is empty now."
                    topdrawer_items = 'empty'
                    print ""
                    break
            while "bottom" in action:
                sees = bottomdrawer
                print sees
                action = raw_input("What do you do? > ")
                if action == 'inventory':
                    print inventory
                    continue
                if action == 'health':
                    print health
                    continue    
                while "take" or "pick up" in action:
                    if bottomdrawer_items != 'empty':
                        inventory += ['knife']
                    print inventory
                    print bottomdrawer_statement
                    bottomdrawer_statement = "There is nothing to take."
                    bottomdrawer = "The bottom drawer is empty and looks like the broken bottom could not possible hold anything anymore."
                    bottomdrawer_items = 'empty'
                    print ""
                    break
            continue
        continue
    continue
