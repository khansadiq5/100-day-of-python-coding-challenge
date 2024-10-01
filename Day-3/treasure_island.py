print(r'''
                            ._.
                        ,'   ^-_
                      ,'     ,' `.
                     /      /     `.
                    /|     l        `.
                   /  `..^.|   .-.    \
                   \   /   `. /   `.  ,'"'.
                    >--\     /      \/ _   \
                   / _-^    i       o\(*)   i
                  /,'       l         |~    |
                  V         '.       /\    /
                              `-___-'  '--:
                                 \         \
                                  \ (_      \,-;
                                   \  '-----' /
                                    \         |
                                     \       /
                                      |     /
                                      |    /
                                     /    /
                   _----_     ,-.===/'. ,'  _------_
                _-^      ^-__/,'***/'.,'__-^        `.
             _-^          / //____/ ,'*\\\            `.
           ,'            | ||###,','`.**||\             \
          /              | ||_-','####\*|| |             |
         |               |  \\-^#######`|| |      |      |
         |                \  \`.######,' ! |      |     /.
         |                 \  \ `----' ,'  |      |       \
         ,\        \        \  `------'/  /       |        \
        /  `        |        \  \     /  /        |         |
       /           /          \  \   /  /         !         |
      /           /.           \  \ /  /        ,:\          \
     |           /\ `.          \  Y  /       ,'/  \  __-----_\
    ,|          /  \  `-------   \  \/  -----' /    \/...--...`\
   / __---__  ,'    `.           /\  \        /     |' ..--...`.|
  /,'...-...`.        `:        /  \  \     ,'       \'       '/
  |.'...-...'|          \      /  / \  \  ,'         |        /
  \.'       '|           \    /  /   \  \'/__       /        /
   \        /            .`--'--'-----`--`.  \   _-'        /
    |       `-^.  ,--.   |________________||~',-/          |
    |           `'   /  /                  |  \/          /
    |          ._--~^   |                  |  |          |
    !          |        |                  |  i\   /__/_-'
     \      \  \        \      ,'~~~~i     | /  `~'
      `.  \`.\  :        \    i      |     L/
        \  | `| |        |    |      |    |
         \_/  `-'        |    |      |    |
''')

print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")

choice1 = input("You're at a cross road. Where do you want to go? Type 'left' or 'right' \n").lower()

if choice1 == "left":
    choice2 = input("You come to a lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. \n").lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, One yellow and One blue. Which color do you choose? \n ").lower()
        if choice3 == "yellow":
            print("You found the treasure! You Won!")
        elif choice3 == "red":
            print("It's a room full of fire. Game Over!")
        elif choice3 == "blue":  
            print("You enter a room of beasts. Game Over")  
        else:
            print("You chose a door that doesn't exist. Game Over!")    
    else:
        print("You got attacked by an angry trout. Game Over!")    
else:
    print("You fell into a hole. Game Over!")    
