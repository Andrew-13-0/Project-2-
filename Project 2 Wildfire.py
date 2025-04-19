class Impact:
    def __init__ (self, address,biome,damage):
        self.address = address
        self.biome = biome
        self.damage = damage
        self.FireSpreadChance = 0

    def FireSpreadAssessment(self, RalativeHumidityPercent, WindSpeedPercent ):
        if  RalativeHumidityPercent <= 0.15 :
            self.FireSpreadChance += 1
            print( "The humidity icreases the likelyhood of fire spreading.")
        else:
            print( "The humidity decreases the likelyhood fire spreading." )
        
        if  WindSpeedPercent >= 0.1 :
            self.FireSpreadChance += 1
            print(" the wind speed increases the likelyhood of spreading fire")
        else:
            print( "the wind speed decreases the likelyhood of spreading fire" )
        if self.FireSpreadChance == 0:
            print("Assessment: Safe")
        elif  self.FireSpreadChance == 1:
            print("Assessment: Caution")
        elif self.FireSpreadChance == 2 :
            print("Assessment: Danger")
        
Person1 = Impact("13235 Impact Ave 17333 ", "Forest", "Severely Damaged" )
Person1.FireSpreadAssessment(.34, .43)
class HelpQueue:
    def __init__ (self):
        self.queue = []
        self.Pqueue = []
        
    def AddStrandardQueue(self,person):
        self.queue.append(person)
        print(f"{person} is added to queue")
    
    def AddPriorityQueue(self,person):
        self.Pqueue.append(person)
        print(f"{person} is added to Priority queue")

    def removeQueue(self):
        if len(self.Pqueue) > 0:
            person = self.Pqueue.pop()
            print(f"{person} removed from Priority queue")
        elif len(self.queue) > 0:
            person = self.queue.pop()
            print(f"{person} removed from queue")
        else:
            print("No one in queue")



print ("\n------ Adding to queue ------\n" )

Queue1 = HelpQueue()

Person1 = Queue1.AddStrandardQueue("Bill")
Person2 = Queue1.AddStrandardQueue("Ted")
Person3 = Queue1.AddStrandardQueue("Bob")

Person4 = Queue1.AddPriorityQueue("Amy")
Person5 = Queue1.AddPriorityQueue("Jill")
Person6 = Queue1.AddPriorityQueue("Mandy")

print(Queue1.queue)
print(Queue1.Pqueue)

print ("\n------ Removing from queue ------\n" )

Queue1.removeQueue()
Queue1.removeQueue()
Queue1.removeQueue()
Queue1.removeQueue()
Queue1.removeQueue()
Queue1.removeQueue()
