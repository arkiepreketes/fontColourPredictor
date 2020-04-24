import random
#Helper RGB function
def from_rgb(rgb):
    return "#%02x%02x%02x" % rgb

#Helper to produce a random RGB tuple
def getRGB():
    r = random.randrange(0,256) 
    g = random.randrange(0,256) 
    b = random.randrange(0,256) 
    return (r,g,b)

