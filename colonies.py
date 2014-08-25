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
        self.type = self.chooseRandomPlanetType()
        
    def generateRandomName(self):
        #uses the "randomname lists" to generate a name
        #issue is names have a chance of not being unique
        prefix = Planet.prefixes[random.randrange( len(Planet.prefixes))]
        middle = Planet.middles[random.randrange( len(Planet.middles))]
        suffix = Planet.suffixes[random.randrange( len(Planet.suffixes))]

        name = prefix + middle + suffix

        return name

    def chooseRandomPlanetType(self):
        terraintype = Planet.planettypes[random.randrange( len(Planet.planettypes))]
        return terraintype


#Code beyond here is primarily used to test features and the code
def main():
    PLANETLIST = []
    count = 0

    while count <> 20:
        PLANETLIST.append(Planet())
        count +=1

    for p in PLANETLIST:
        print "ID: " + str(p.ID)
        print "Name: " + p.name
        print "Type: " + p.type

main()
