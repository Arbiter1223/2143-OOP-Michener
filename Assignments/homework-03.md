# Cory Michener

### Questions

**1)** What does Python print for each of the following:

```python 
johns_bag = Bag()
johns_bag.print_bag()
# what prints?

for color in [’blue’, ’red’, ’green’, ’red’]:
    johns_bag.add_skittle(Skittle(color))
johns_bag.print_bag()
# what prints?

s = johns_bag.take_skittle()
print(s.color)
# what prints?

print(johns_bag.number_sold)
# what prints?

print(Bag.number_sold)
# what prints?

soumyas_bag = Bag()
soumyas_bag.print_bag()

print(johns_bag.print_bag())
# what prints?

print(Bag.number_sold)
# what prints?

print(soumyas_bag.number_sold)
# what prints?
```

### Answer 1

```python
# answers here
[]
['blue', 'red', 'green', 'red']
blue
1
1
[]
['red', 'green', 'red']
None
2
2
```

**2)**  Write a new method for the Bag class called take color, which takes a color and
removes (and returns) a Skittle of that color from the bag. If there is no Skittle
of that color, then it returns `None`.

```python
def take_color(self, color):






```


### Answer 2

```python
# answer here
    def take_color(self, color):
        """Take a color, and remove a single Skittle of that color from bag. Return."""
        for i in self.skittles:
            if (color == i.color):
                self.skittles.remove(i)
                return i.color
```

**3.** Write a new method for the Bag class called take all, which takes all the Skittles
in the current bag and prints the color of the each Skittle taken from the bag.

```python
def take_all(self):




```

### Answer 3

```python
# answer here
    def take_all(self):
        """Take all the skittles out, and print the color of each one"""
        for i in self.skittles:
            print(i.color)
        self.skittles.clear()
```