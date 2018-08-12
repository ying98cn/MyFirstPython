import sys
from math import cos, radians

# example: 
## Create a string with spaces proportional to a cosine of x in degrees
#def make_dot_string(x):
#    rad = radians(x)                             # cos works with radians
#    numspaces = int(20 * cos(radians(x)) + 20)   # scale to 0-40 spaces
#    st = ' ' * numspaces + 'o'                   # place 'o' after the spaces
#    return st

#def show_dots_graph():
#    for i in range(0, 1800, 12):
#        s = make_dot_string(i)
#        print(s)

#def main():
#    show_dots_graph()

#main()


# example: plotted graphically
import numpy as np     # installed with matplotlib
import matplotlib.pyplot as plt

def main():
    x = np.arange(0, radians(1800), radians(12))
    plt.plot(x, np.cos(x), 'b')
    plt.show()

main()

