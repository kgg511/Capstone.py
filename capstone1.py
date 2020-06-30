# Where I am currently: function makeOutfitMyself allows user to select an outfit choice from each category, adds it to a list, and returns the complete outfit.
# function computerChooses() has not been designed yet
# I plan on later adding in color options or allowing the user to add their own options
import random
gChoices = []
DictionaryClothing = {'head options:': 'baseball cap wig sombrero beret fedora toupee'.split(),
                      'chest options': 'blouse dress shirt tanktop bikini t-shirt sweater chestplate corset'.split(),
                      'leg options:':
                          'leggings skinny-jeans khaki\'s shorts daisy-dukes skirt bike-shorts tutu'.split(),
                      'feet options:':
                          'running-shoes tap-dance-shoes clogs stilettos platform-shoes sandals flipflops cowboy-boots'.split(),
                      'accessory options:':
                          'belt purse necklace headband hoop-earrings sword bow mustache goatee glasses'.split()}
# def computerChooses():
# The computer selects a random clothing option for each clothing category
# for every keyValues in DictionaryClothing:
# randomIndex = (random.randint(1, len((keyValues)-1)
# Return key[randomIndex]

def makeOutfitMyself():
    # The user selects a choice for each category
    Choices = []
    for item in DictionaryClothing:
        print(item)
        print(DictionaryClothing[item])
        response = ''
        while response not in DictionaryClothing[item] and response != 'CC':
            print("please select one of the choices, or type ‘CC’ to have the computer do it for you")
            response = input()
        Choices.append(response)
    return Choices
            # If input() in values:
            # Return input()
            # Else:
            # randomIndex = (random.randint(1, len((key values)-1)
            # Return key[randomIndex]


print("""Everyday most people must choose an outfit to wear.This game, 'Dress My Day', is here to help you design outfits.
Type MC (my choice) to make one yourself, or CC (computer choice) to have the computer make it for you.
If you make it yourself, you will be asked a series of questions about clothing type and color.
Select one of the given options by typing it in.
At any point you can respond to a question by typing “CC” and the computer will make that specific choice.
At the end, you will be told your outfit.""")
response = input()

if response == 'MC':
    gChoices = makeOutfitMyself()
    # Else:
     # Choices.append(ComputerChooses())
# print('The outfit is now done. The outfit is: ’)
# print(Choices)
print('Looks like your outfit is: ')
for item in gChoices:
    print(item)
print('Hope you enjoyed')
