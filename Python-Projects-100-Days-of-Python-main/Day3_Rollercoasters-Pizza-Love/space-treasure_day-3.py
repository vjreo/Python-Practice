#!/usr/bin/env python
# coding: utf-8

# In[3]:





# In[8]:


import time

print('Welcome to the Interstellar Treasure Hunt! Your mission, should you choose to accept, is to navigate this map \nand find the treasure. May the odds ever be in your favor...')
time.sleep(2.5)
user = input('\nChoose a unique username to be called along your journey. ')
user_name = user.upper()
mission_accept = input(f'\n{user_name}, do you accept this challenge? Yes or No. ')
mission_begin = mission_accept.lower()

if mission_begin == 'yes':
    print(f'\nLet us begin our journey then, {user_name}.')
else:
    print(f'\nGame over {user_name}.')
    
time.sleep(5)
print('\nWhat are you waiting for? We\'ve got treasure to hunt. Jump in. I call this trusty steed Ole Faithful.\nShe was built back on Mars before intergallactic travel became so commonplace. We used her to planet hop...\nbefore pioneering became cool and exploration was all the rage again. Well, I\'m talking too much. Why don\'t you get\nsome shut-eye while I get her ready to roll. Once we hit the jetstream, I\'ll wake ya up...until then, rest easy.\nYou\'ll thank me later...')

time.sleep(10)
print(f'\n{user_name}, how\'d the nap feel sleeping beauty? Doesn\'t matter because we are coming up on our first space\nobstacle.\nThere are two routes:\nThe first, a right curving hyperloop will put us on Jupiters\'s 53rd moon. From there, we can hop onto the \nintergallactic byway that takes us to Saturn.\nThe second route is to continue straight past Jupiter to make a faster time to conserve energy for a pitstop at \nUranus.')
time.sleep(3)
route = input('\nWhich route do you want to take? One or Two. ' )
route_lower = route.lower()

if route_lower == 'one':
    print(f'\nGood choice, {user_name}. Route 2 skipped Saturn which is the next planet in the solar system after Earth and Mars if \norbiting clockwise around the sun. Let\'s continue the search for tresure!')
else:
    print(f'\nGame over {user_name}.')
    
time.sleep(3)
print(f'\nThat wasn\'t too bad, but great navigating. Up ahead we will enter warp speed in order to enter the wormhole where the treasure is located. Just past the entrance of the wormhole there is a fork in its shape. Based on your calculations, do we go left or right?')
direction = input('\nDo we go left or right once in the wormhole? Enter Left or Right. ')
direction_lower = direction.lower()

if direction_lower == 'right':
    print(f'WAHOOOO, we did it {user_name}! One more interstellar obstacle and we should find the treaure! Nice work, rookie!')
else: 
    print(f'\nGame over {user_name}.')
    

time.sleep(3)
print(f'\nWell we made it to the final stretch {user_name}. I know it\'s dark in here, but thankfully Ole Faithful has these trusty \nheadlights to help us look around. From the lore about this wormhole, there is point at which three glowing stars \nlight the way to the exit and ultimately, the otherside where the treasure was lost.')
time.sleep(3)
print(f'\nThere! Look {user_name}, those are the three stars. Okay, think about this. Which star we choose decides on whether we end up somewhere unheard of. We\'re getting close, so make a decision!')
time.sleep(3)
choice = input('\nWhich start should we choose? Enter Red, Blue, or Green')
choice_lower = choice.lower()

if choice == 'red':
    print(f'Game Over {user_name}. The first start transported you to Azkaban. Have fun with Sirius!')
elif choice == 'green':
    print(f'Game Over {user_name}. The third star teleported you to the Death Star to live under Vader\'s tutelage.')
else: 
    print(f'Mission accomplished {user_name}. You found the treasure!')
    time.sleep(2)
    print('''

*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')


# In[ ]:




