class Intro:
    def intro(self):
        print("Were no strangers to love\nYou know the rules and so do I\nA full commitments what Im thinkin of\nYou wouldnt get this from any other guy\n")
        
class PreChorus(Intro):
    def prechorus(self):
        print("I just wanna tell you how I'm feeling\nGotta make you understand\n")

class Chorus(PreChorus):
    def chorus(self):
        print("Never gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you\n")

class Verse:
    def verse(self):
        print("We've known each other for so long\nYour heart's been aching, but you're too shy to say it\nInside, we both know what's been going on\nWe know the game and we're gonna play it\n")
        
class Prechorustwo(Verse, Chorus):
    def prechorustwo(self):
        print("And if you ask me how I'm feeling\nDon't tell me you're too blind to see\n")
        

Part1 = Chorus()
Part2 = Prechorustwo()
Part1.intro()
Part1.prechorus()
Part1.chorus()
Part2.verse()
Part2.prechorustwo()
Part2.chorus()
Part2.chorus()
Part2.verse()
Part2.prechorustwo()
Part2.chorus()
Part2.chorus()
Part2.chorus()