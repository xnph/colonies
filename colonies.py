#Colonies - Space colony management sim
#Created by Bhavish J (Github: xnph)

#Learning python and github. Two birds with one stone.

import random


class Planet:
    """Class representing planets and handles generation and properties of
planets and such"""
    planetcount = 0 #each planet will have an id
    
    planettypes = ["desert","ocean","terra"] #will add more types later on

    #Lists used in random name generation
    prefixes = ["As","An","Ba","Br","Ca","Ce"]
    middles = ["ara","leth","exer","olor","sam"]
    suffixes = ["ason","bas","ceres","loth","xis"]
    
    def __init__(self):

        Planet.planetcount += 1 #becomes ID
        
        self.ID = Planet.planetcount
        self.name = self.generateRandomName()

    def generateRandomName(self):
        #uses the "randomname lists" to generate a name
        #issue is names have a chance of not being unique
        prefix = Planet.prefixes[random.randrange( len(Planet.prefixes) - 1 )]
        middle = Planet.middles[random.randrange( len(Planet.middles) - 1 )]
        suffix = Planet.suffixes[random.randrange( len(Planet.suffixes) - 1 )]

        name = prefix + middle + suffix

        return name

a = Planet()
b = Planet()
c = Planet()

print a.name
print a.ID
print b.name
print b.ID
