#start program

import os #allows bolding of text to work

#variables
txt = 0
score = 0
restart = 0
numbers = [0, 1, 2, 3] #room for error - hence extensive list.
info = 0
os.system('cls') 

#Intro
print('------------------------------------------------------------------------------------------------------------------------------------')
print('                             Welcome to Bakr.io! This program is going to allow you to choose your own                              ')
print('                       types of bread to be discovered in a text of your choice. You will then have the option                      ')
print('                  to learn about your desired bread type. Please follow the step by step instructions provided!                     ')
print('')
print('')
print('')

#iteration loop
while score == 0: 
    breadtype = (input("Please enter a bread type you would like to search for:"))
    print('')
    score = int(input("If you would like to include another type of bread enter '0', if not enter '1'"))
    print('')

#iteration loop    
for restart in numbers:
    txt = (input("Awesome! Now that we know what bread you're looking for, please add the text you wished to be scanned:"))
    print('')
    if breadtype in txt: #selection loop 
        print("The word \033[1m", breadtype, "\033[0m has been identified in the text:", txt) #returning the text with breadtype in bold
        info = int(input("Would you like to know some information and tips about your bread? (enter 1 for yes and any other number for no):"))
        if info == 1:
            if breadtype == 'rye':
                print('It can be light or dark in color, depending on the type of flour used and the addition of coloring')
                print('agents, and is typically denser than bread made from wheat flour. Compared to white bread, it is higher')
                print('in fiber, darker in color, and stronger in flavor. Rye bread was considered a staple through the Middle Ages.')
                print('')
                print('That is the end of the bakr bread search, we hope you have enjoyed the experience.')
            elif breadtype == 'white':
                print('White bread isnt all bad. Although white bread is highly refined and stripped of many of its natural nutrients,')
                print('manufactures do add some of these nutrients back in along with others, including iron, folic acid, riboflavin,')
                print('thiamine, niacin, and sometimes calcium.')
                print('')
                print('That is the end of the bakr bread search, we hope you have enjoyed the experience.')
            elif breadtype == 'brioche':
                print('Its a soft, lightly sweet, rich bread that works in sweet and savoury dishes alike. The reason brioche is so')
                print('light and tastes so rich is because its made with an enriched dough,which gives it that soft texture and')
                print('amazing taste.')
                print('')
                print('That is the end of the bakr bread search, we hope you have enjoyed the experience.')
            elif breadtype == 'multigrain':
                print('Multigrain bread often contains white flour and includes grains, which provide fiber that is good for')
                print('your digestive health. Multigrain bread also tends to have a lower glycemic index than white bread.')
                print('')
                print('That is the end of the bakr bread search, we hope you have enjoyed the experience.')
            elif breadtype == 'sourdough':
                print('When baking sourdough bread, its important that your starter is strong and active. If its been dormant')
                print('in the refrigerator, pull it out and give it a few feeds at room temperature so it starts rising and falling')
                print('within the course of a day.')
                print('')
                print('That is the end of the bakr bread search, we hope you have enjoyed the experience.')
            elif breadtype == 'gluten-free':
                print('For a good rise to occur in your gluten-free dough, the right ingredients need to be used. The ingredients that')
                print('most impact the rise of gluten-free bread include yeast, sugar, xanthan gum, baking soda, and/or baking powder,')
                print('depending on your recipe and type of bread being made.')
                print('')
                print('That is the end of the bakr bread search, we hope you have enjoyed the experience.')
            elif breatype == 'ciabatta':
                print('Ciabatta is baked with a much higher hydration level, making the holes within the dough much bigger than a baguette.')
                print('Ciabatta is also baked with a much stronger flour, which has a more delicate and sweet taste.')
                print('')
                print('That is the end of the bakr bread search, we hope you have enjoyed the experience.')
            restart = input('5')
        
    else:
        print('Sorry, the bread type', breadtype, 'has not been identified in the provided text.') #if doesn't match criteria, repeat loop
        restart = restart + 4


