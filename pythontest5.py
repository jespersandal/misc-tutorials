import random
#stest = "This is a string. It has a funny word bananas. "
#bananatest = stest.find("bananas")
#if (bananatest >=0):
#    bananacount = stest.count("bananas")
#    print "There are " + str(bananacount) + " bananas in stest"
#else:
#    print "There are 0 bananas in stest"

classes = ('fighter', 'cleric', 'wizard', 'ranger', 'druid', 'rogue', 'barbarian', 'bard', 'warlock', 'sorcerer')
maxclassroll = len(classes); maxclassroll -= 1
races = ('human', 'dwarf', 'elf', 'gnome', 'halfling', 'half-orc')
maxraceroll = len(races); maxraceroll -= 1
alphabets = ("wratygbnaeilkheyixtzanorfdwuiyszlpauos", "afannwaaxwpfofnwafn", "ilszxyvziythlti", "egjeknmlcbvnaiuklpmnsggdveea",
              "jespersteinsandal", "abcdefghijklmnopqrstuvwxyz", "tarwgyrrahlhmrwqggnaeeylmnitrwkhga")
abilities = ('STR: ', 'DEX: ', 'CON: ', 'INT: ', 'WIS: ', 'CHA: ')

# Name generator

def generateName():
    maxalphabets = len(alphabets); maxalphabets -= 1
    alphabetpick = random.randint(0,maxalphabets)
    letters = alphabets[alphabetpick]
    maxletter = len(letters); maxletter -= 1
    firstname = ""
    lastname = ""
    firstnamelength = random.randint(2,10)
    lastnamelength = random.randint(2,14)
    for f in range(0,firstnamelength):
        nextletter = letters[random.randint(0,maxletter)]
        firstname = firstname + nextletter
    for l in range(0,lastnamelength):
        nextletter = letters[random.randint(0,maxletter)]
        lastname = lastname + nextletter
    heroname = firstname + " " + lastname
    heroname = heroname.title();
    return heroname;

def prerollstats(race):
    prerolled = [15, 14, 13, 12, 10, 8];
    rerolled = random.shuffle(prerolled)
    if (race == 'human'):
        for i in range(0,5):
            prerolled[i] += 1
        return prerolled;
    elif (race == 'dwarf'):
        prerolled[2] += 2
        prerolled[4] += 2
        return prerolled;
    elif (race == 'elf'):
        prerolled[1] += 2
        prerolled[3] += 2
        return prerolled;
    elif (race == 'gnome'):
        prerolled[3] += 2
        prerolled[5] += 2
        return prerolled;
    elif (race == 'halfling'):
        prerolled[1] += 2
        prerolled[4] += 2
        return prerolled;
    elif (race == 'half-orc'):
        prerolled[0] += 2
        prerolled[2] += 2
        return prerolled;
    else:
        return prerolled;

def createCharacter():
    racepick = random.randint(0,maxraceroll)
    classpick = random.randint(0,maxclassroll)
    heroname = generateName()
    print "\n", heroname
    print races[racepick] + " " + classes[classpick]
    stats = prerollstats(races[racepick])
    for i in range(0,6):
        print abilities[i] + str(stats[i])
    return

print "Your party: \n"
for i in range(0,5):
    createCharacter();

