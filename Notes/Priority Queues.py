# Priority Queue?
# FIFO - First In First Out

# Provide user with two things
#    Enqueue - put items in queue
#    Denqueue - take items out of queue

# Data members
#    Front
#    Rear

# if (front == rear)
#    Queue is empty

# Add item to Queue
#    Find Read
#    insert 8
#    Update Rear by one

# Take item out
#    Find front
#    8 still kinda exists in memory
#    Update front

# All depends on where FRONT and REAR are

# Priority Queues add items to list based on priority
# Triage Priorities
# 1. Respitory Distress (RD)
# 2. Bleeding Profusely (Bleeder)
# 3. Sniffles           (Sniffs)

# Person
#    First name (string)
#    Last name (string)
#    ID (int)
#    Priority (int)
#    Time (int)
#    Rank (string)

import time
import random

class Person(object):
    def __init__(self, fname = "N/A", lname = "N/A", rank = "N/A", ID = 0000000000, priority = 0):
        self.fname = fname
        self.lname = lname
        self.rank = rank
        self.ID = ID
        self.time = time.ctime()
        self.priority = priority

    def __str__(self):
        return "%s, %s, %s, %d, Priority: %d, %s" % (self.lname, self.fname, self.rank, self.ID, self.priority, self.time)

#    def __repr__(self):
#        temp = " ".join()
#        return temp

class PriorityQueue(object):
    def __init__(self):
        self.pQueue = []

    def addPerson(self, x):
        if len(self.pQueue) == 0:
            self.pQueue.append(x)
        elif x < self.pQueue[0]:
            self.pQueue.insert(0, x)
        elif x > self.pQueue[-1]:
            self.pQueue.append(x)
        else:
            for i in range(len(self.pQueue)):
                if x < self.pQueue[i]:
                    self.pQueue.insert(i, x)
                    break
                
                
    
    def removePerson(self):
        pass

    

p1 = Person("Frank", "Loyd", "Sergeant", 5545122376, 3)
print (p1)
p2 = Person("Sue", "Loyd", "Private", 1223455678, 2)
print (p2)

L = []
L.append(p1)
L.append(p2)

print (L)

pq = PriorityQueue()
for i in range(20):
    pq.addPerson(random.randint(0, 100))

print (pq)