


class Monster:
    monstername = ""
    hitpoints = 1
    ac = 10

    def __init__(self, name):
        self.monstername = name

    def sethitpoints(self, hp):
        hitpoints = hp

    def changehitpoints(self, hp):
        int(hp);
        hitpoints = hitpoints + hp
    
    def currenthitpoints(self):
        return self.hitpoints;


beholder = Monster("Beholder")
print "This monster has ", beholder.currenthitpoints(), " hit points left"


    
