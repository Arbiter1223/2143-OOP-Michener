# Cory Michener

class Pet(object):
    def __init__(self, name, owner):
        self.is_alive = True # It’s alive!!!
        self.name = name
        self.owner = owner
    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")
    def talk(self):
        print("...")

class Dog(Pet):
    def __init__(self, name, owner, color):
        Pet.__init__(self, name, owner)
        self.color = color
    def talk(self):
        print("Woof!")

# Question 1: Write the Cat class and lose_life method
# Answer 1
class Cat(Pet):
    def __init__(self, name, owner, lives = 9):
        Pet.__init__(self, name, owner)
        self.lives = 9

    def talk(self):
        print("Meow!")

    def lose_life(self):
        if self.is_alive:
            self.lives = self.lives - 1
            print(self.lives)
            if self.lives == 0:
                self.is_alive = False
                print(self.name + " died.")
        else:
            print("Your cat is already dead.")

# Question 2
class Foo(object):
    def __init__(self, a):
        self.a = a
    def baz(self, val):
        return val
    def garply(self):
        return self.baz(self.a)

class Bar(Foo):
    a = 1

f = Foo(4)
b = Bar(3)
print(f.a)
# prints what ?
# Answer: 4

print(b.a)
# prints what ?
# Answer: 3

print(f.garply())
# prints what ?
# Answer: 4

print(b.garply())
# prints what ?
# Answer: 3

b.a = 9
print(b.garply())
# prints what ?
# Answer: 9

f.baz = lambda val: val * val
print(f.garply())
# prints what ?
# Answer: 16