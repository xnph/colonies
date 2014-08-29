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
        """random generation of the Planet's properties"""
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

class Game:
    """Class with master functions, initialisations and variables"""

    def __init__(self):
        self.PLANETLIST = [] #stores all planets

        
        self.NUMPLANETS = 20 #number of planets to generate
        self.MAXEDGES = 3 #Maximum number of edges between planets
        
    def initialisePlanets(self):
        """generates random planets"""
        PLANETLIST = self.PLANETLIST #stores all planets in a copy of Game.PLANETLIST
        NUMPLANETS = self.NUMPLANETS #number of planets to generate
        count = 0

        while count <> NUMPLANETS:
            PLANETLIST.append(Planet())
            count +=1

        
        self.generatePlanetEdges(PLANETLIST)
##        FUN BIT TO SEE ALL THE PLANETS
##        for p in PLANETLIST:
##            print "ID: " + str(p.ID)
##            print "Name: " + p.name
##            print "Type: " + p.type
##            print "ADJLIST: " + str(p.adjlist) + "\n"
        
    def generatePlanetEdges(self, PLANETLIST):
        """Creates the connections between planets"""
        maxlinks = self.MAXEDGES #the maximum number of edges between planets
        
        
        
        for p in PLANETLIST: #for each planet in PLANETLIST
            
            VALIDLIST = list(PLANETLIST) #copy of planetlist
            VALIDLIST.remove(p) #remove the planet itself from the list of planets

            #then select 3(or maxlinks) random planets to link to
            count = 0
            while count <> maxlinks:
                randnum = random.randrange(0,len(VALIDLIST)-1) # a random planet
                p.adjlist.append(VALIDLIST[randnum].ID)# add random planet to adjlist
                VALIDLIST.remove(VALIDLIST[randnum])#remove that planet from valid list
                count += 1
                
    def mainLoop(self,player):
        pass
            
class Player:
    """class representing the player of the game, stores current planet pos"""
    def __init__(self):
        self.LOCATION = 1
        self.NAME = self.setName()
        self.ACTIONLIST = ["Describe","Warp"] #list of possible actions
    def setName(self): #set player name
        print("What is your name?")
        name = raw_input(">")

        print("Welcome to Colonies!")
        return name        

    def setLocation(self,planet): #set player's location, Planet Obj passed in
        self.LOCATION = planet.ID

    def describeLocation(self,PLANETLIST):
        currentplanetindex = self.LOCATION

        planetname = PLANETLIST[currentplanetindex].name
        planettype = PLANETLIST[currentplanetindex].type
        print ("This is " + planetname + ", it is a " + planettype + " type")
        
    def warp(self):
        currentplanet = Game.PLANETLIST[self.location] #the planet the player is on

        count = 0
        

        print("The following planets are available for warp:")

        for name in currentplanet.ADJLIST: #prints out each planet's name
            count += 1
            print count + ". " + name 

        choice = 0
        adjlistlength = len(currentplanet.ADJLIST)
        while (choice <= 0) or choice > adjlistlength:
            print("Select a planet to warp to:")
            choice = raw_input(">")
            
        
        
        
            
#Code beyond here is primarily used to test features and the code
def main():
    game = Game() #init gameobject
    game.initialisePlanets() #load planetlist

    
    
    player = Player()
    player.describeLocation(game.PLANETLIST)
        
main()
