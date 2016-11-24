import time

health = 10
inventory = ['clothes']
player_name = raw_input("What is your name? > ")

"""world items"""
topdrawer_items = 'full'
bottomdrawer_items = 'full'


"""Statements about stuff"""
topdraweritem_statement = "You take the health potion"
bottomdraweritem_statement = "You take the rusty iron knife"


"""World Descriptions"""

#Bridge
sees_overbridge = "You see a path leading under the bridge. In the distance there is the broken windmill."
sees_underbridge = "Under the bridge is dark with thick, wet moss growing through the cobble cracks, dripping like living green stalactites as they hang from the damp stone ceiling. You see a small door under the bridge, the cracks around the edges illuminated by a thin light causing dancing shadows to play across the rippling brook water"
sees_roomunderbridge = "A cramped alcove illumintated by a single flickering torch is revealed as the door is opened. Within is a small wooden dresser with two drawers, a top drawer and a bottom drawer. The dresser looks old." 
sees_topdrawer = "You find a healing potion. It glows with inner light."
sees_bottomdrawer = "The drawer bottom crumbles from decay as it is opened. A rusty iron knife clatters to the ground."

loc_overbridge = "You are standing on small stone bridge overlooking a brook."
loc_underbridge = "You are standing under the bridge."
loc_roomunderbridge = "You are in a small hidden room under the bridge."



#Windmill
sees_windmill = "You see that the structure has a wooden door standing adjar and swinging in the gentle breeze. The wooden windmill blades have rotted and fallen off long ago"
sees_windmillfloor = "You see a stone spiral staircase winding around the outside of the room to the second floor. In the middle is a glass chandelier hanging crookedly on the ceiling. In the right corner there is a crushed desk laying on the ground. On the left corner is a small door."
sees_windmillstairup = "You climb the staircase."
sees_windmillstairdown = "You decend the staircase."
sees_windmillfloor2 = "The second floor is a large open room that has a large device that looks like it was used to grind flour. On one wall there is a small staircase that goes to the third floor. Behind is a stair down. A giant mural of the windmill is on the opposite wall."
sees_windmillfloor3 = "The third floor is a another large open room that has many boxes and bags. It appears to be a storage room. In the left corner is a small door like the one on the first floor."
sees_windmillsecret1 = "The room is a small square tower going all the way up to the third floor. On one wall there is a small platform that appears to be able to hoist you up to the top floor. On all the other walls there are pegs with rope tied in a circle around the room. All the pegs appear empty except the three at the top which you cannnot see. A lever is on your right."
sees_windmillsecret2 = "You are on a small platfrom. Next to you is the elevator shaft that you saw on the first floor. The three hooks you saw have decaying bodies hanging with ropes around their necks. The smell is horrifying"

loc_windmill = "You are at the broken windmill."
loc_windmillfloor = "You are inside the windmill on the first floor."
loc_windmillfloor2 = "You are on the second floor of the windmill."
loc_windmillfloor3 = "You are on the third floor of the windmill."
loc_windmillsecret1 = "You are in on the first floor of a tiny alcove."
loc_windmillsecret2 = "You are on a platform on the third floor of the windmill."


location = loc_overbridge
sees = sees_overbridge

while True:
    print '\n\n'
    print location
    print sees
    action2 = ''
    action1 = raw_input("What do you do? >")
    if action1 == 'inventory':
        print inventory
    if action1 == 'health':
        print "%s's Health is %s" % (player_name, str(health))
    if location == loc_overbridge:
        if "under" in action1:
            location = loc_underbridge
            sees = sees_underbridge
            action1 = ''
        if "windmill" in action1:
            location = loc_windmill
            sees = sees_windmill
            action1 = ''            
    if location == loc_underbridge:
        if "door" in action1:
            location = loc_roomunderbridge
            sees = sees_roomunderbridge
            action1 = ''
        if "leave" in action1:
            location = loc_overbridge
            sees = sees_overbridge
            action1 = ''
        if "above" in action1:
            location = loc_overbridge
            sees = sees_overbridge
            action1 = ''
        if "inside" in action1:
            location = loc_roomunderbridge
            sees = sees_roomunderbridge
    if location == loc_roomunderbridge:
        if "bottom" in action1:
            location = loc_roomunderbridge
            sees = sees_bottomdrawer
            action1 = ''
            print sees
            action2 = raw_input("What do you do? >")
            if "pick" in action2:
                if bottomdrawer_items != 'empty':
                    inventory += ['knife']
                print bottomdraweritem_statement
                bottomdraweritem_statement = "There is nothing to take."
                sees_bottomdrawer = "The bottom drawer is empty and looks like the broken bottom could not possible hold anything anymore."
                bottomdrawer_items = 'empty'
            if "take" in action2:
                if bottomdrawer_items != 'empty':
                    inventory += ['knife']
                print bottomdraweritem_statement
                bottomdraweritem_statement = "There is nothing to take."
                sees_bottomdrawer = "The bottom drawer is empty and looks like the broken bottom could not possible hold anything anymore."
                bottomdrawer_items = 'empty'
                
            else:
                location = loc_roomunderbridge
                sees = sees_roomunderbridge
                action1 = ''
        if "top" in action1:
            location = loc_roomunderbridge
            sees = sees_topdrawer
            print sees
            action2 = raw_input("What do you do? >")
            if "take" in action2:
                if topdrawer_items != 'empty':
                    inventory += ['health potion']
                print topdraweritem_statement
                topdraweritem_statement = "There is nothing to take."
                sees_topdrawer = "The top drawer is empty."
                topdrawer_items = 'empty'
            if "pick" in action2:
                if topdrawer_items != 'empty':
                    inventory += ['health potion']
                print topdraweritem_statement
                topdraweritem_statement = "There is nothing to take."
                sees_topdrawer = "The top drawer is empty."
                topdrawer_items = 'empty'
            else:
                location = loc_roomunderbridge
                sees = sees_roomunderbridge
                action1 = ''
        if "leave" in action1:
            location = loc_underbridge
            sees = sees_underbridge
            action1 = ''
        if "exit" in action1:
            location = loc_underbridge
            sees = sees_underbridge
            action1 = ''
        if "door" in action1:
            location = loc_underbridge
            sees = sees_underbridge
            action1 = ''
    if location == loc_windmill:
        if "door" in action1:
            location = loc_windmillfloor
            sees = sees_windmillfloor
            action1 = ''
        if "enter" in action1:
            location = loc_windmillfloor
            sees = sees_windmillfloor
            action1 = ''
    if location == loc_windmillfloor:
        if "up stairs" in action1:
            location = loc_windmillfloor2
            sees = sees_windmillfloor2
            action1 = ''
        if "hidden" in action1:
            location = loc_windmillsecret1
            sees = sees_windmillsecret1
            action1 = ''
        if "small door" in action1:
            location = loc_windmillsecret1
            sees = sees_windmillsecret1
            action1 = ''
    if location == loc_windmillsecret1:
        if "lever" in action1:
            locattion = loc_windmillsecret2
            sees = sees_windmillsecret2
            action1 = ''
        if "leave" in action1:
            location = loc_windmillfloor
            sees = sees_windmillfloor
            action1 = ''
        if "door" in action1:
            location = loc_windmillfloor
            sees = sees_windmillfloor
            action1 = ''
    if location == loc_windmillfloor2:
        if "up stairs" in action1:
            location = loc_windmillfloor3
            sees = sees_windmillfloor3
            action1 = ''
        if "down" in action1:
            location = loc_windmillfloor
            sees = sees_windmillfloor
            action1 = ''
    if location == loc_windmillfloor3:
        if "down" in action1:
            location = loc_windmillfloor2
            sees = sees_windmillfloor2
            action1 = ''
        if "door" in action1:
            location = loc_windmillsecret2
            sees = sees_windmillsecret2
            action1 = ''
            
