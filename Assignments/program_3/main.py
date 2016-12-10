from PIL import Image
from imageEdit import ImageEd
from io import BytesIO
import urllib.request
import random
import sys

# Get image off internet
# These are the images I used durring debugging
# (I made the first two images myself a while back actually ^_^)
#url = 'http://img12.deviantart.net/90d5/i/2016/006/d/5/the_joy_of_creation_can_somtimes_become_tiring____by_arbiter1223-d9my5c5.jpg'
#url = 'http://img12.deviantart.net/5d0e/i/2015/313/d/c/damn_unresolved_externals_by_arbiter1223-d9g4k6r.jpg'
url = 'https://raw.githubusercontent.com/rugbyprof/2143-ObjectOrientedProgramming/master/Assignments/Program-03/fruit2.jpg'
#url = 'http://img00.deviantart.net/c2de/i/2013/155/8/3/i_ll_give_you_the_moon_by_marilucia-d5kgs9t.jpg'

file = BytesIO(urllib.request.urlopen(url).read())

# Create image object via ImageEd class
image = ImageEd(file)

# The following were the function calls I used for debugging (one at a time)
#image.example()
#image.glass_effect(3)
#image.flip()
#image.blur(3)
#image.posterize(64)
#image.solarize(100)
#image.grayscale()
#image.warhol()

image.showImage()