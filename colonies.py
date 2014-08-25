#Colonies - Space colony management sim
#Created by Bhavish J (Github: xnph)

#Learning python and github. Two birds with one stone.

import random


class Planet:
    """Class representing planets and handles generation and properties of
planets and such"""
    planetcount = 0 #each planet will have an id

    planettypes = ["Desert","Ocean","Terra", "Gas", "Barren", "Ice", "Rocky", "Lava"] #will add more types later on

    #Lists used in random name generation
    prefixes = ["As","An","Ba","Br","Ca","Ce", "Da","Dou", "Ea", "Eg", "Fa", "Fi", "Ga" ,
                "Go", "Ha", "He", "Il" "Ik", "Ja", "Jo", "Ky", "Kr", "La", "L'", "Ma",
                "Mr", "Nar", "Ne", "Or", "Oo", "Pa", "Pi" , "Qe", "Qu", "Ra", "Ry",
                "Sa", "Sk", "Ta" , "Ti", "Ur", "Ua", "Ve", "Vi", "Wa", "We", "Xa", "Xo",
                "Yar", "Yil", "Zo", "Za"]

    middles = ["ara","bac","cara", "door", "exi", "for", "goor", "har", "ilo", "jar" ,
               "kas", "lars", "mor", "noor","oo", "para", "quar", "rely", "so'ra", "tun" ,
               "uvula", "ver", "wari", "xahna", "yool", "zyzz",
               "leth","exer","olor","sam", "'"]

    suffixes = ["ason","bas","ceres","delt", "eran", "fosh", "gras", "hard", "iin",
                "jon", "krom", "lesh", "mon", "nix", "o", "pad", "qu", "rad", "san",
                "tal", "'uve", "vor", "want", "xerex", "yan", "zom"]

    def __init__(self):

        Planet.planetcount += 1 #becomes ID

        self.ID = Planet.planetcount
        self.name = self.generateRandomName()
        self.type = self.chooseRandomPlanetType()
        self.adjlist = [] #represents which planets can be reached from this planet

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
    PLANETLIST = [] #stores all planets
    NUMPLANETS = 10 #generates 10 planets
    count = 0

    while count <> NUMPLANETS:
        PLANETLIST.append(Planet())
        count +=1

    PLANETGRAPH = generatePlanetGraph(PLANETLIST, PLANETLIST[1])

    for p in PLANETLIST:
        print "ID: " + str(p.ID)
        print "Name: " + p.name
        print "Type: " + p.type
        print "ADJLIST: " + str(p.adjlist) + "\n"

#will probably be recursive
def generatePlanetGraph(PLANETLIST, planet): #will loop through all planets and do some shit
    maxedges = 4 #I don't want a ridiculous number of edges between planets
    PLANETGRAPH = {}
    
    
    connectedlist = []
    
    numplanets = random.randrange(1,maxedges) #number of planet links
    PLANETLIST.remove(planet) #remove current planet from list
    count = 0
    while count <> numplanets :
        
        randomplanet = random.randrange(0, len(PLANETLIST))
        connectedlist.append(PLANETLIST[randomplanet])
        PLANETLIST.remove(PLANETLIST[randomplanet])

        count += 1

    PLANETGRAPH[planet] = connectedlist
        
    for p in connectedlist:
        
        generatePlanetGraph(PLANETLIST,p)

    return PLANETGRAPH
        
        
main()

