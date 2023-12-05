import os
import mnist
import random
import numpy as np
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt

# load binary image for a character:
def load_img(filename):
    I = plt.imread(filename)
    I = np.array(I, dtype=bool)
    return I

# load stroke data for a character from text file:
def load_motor(filename):
    # motor: a list of stroke numpy array 
    motor = []
    with open(filename, 'r') as file:
        lines = file.readlines()
    lines =[l.strip() for l in lines]
    for line in lines:
        if line == 'START':
            stroke = []
        elif line == 'BREAK':
            stroke = np.array(stroke)
            motor.append(stroke)
            stroke = []
        else: 
            arr = np.fromstring(line, dtype=float, sep=',')
            stroke.append(arr)
    return motor


# load image and stroke data for a character 
# I [105 x 105 nump]: grayscale image
# drawings: [ns list] of strokes (numpy arrays) in motor space
# lw : line width
# def plot_to_image(I, drawing, lw=2):
#     # strip off the timing data (thrid column)
#     drawing = [d[:, 0:2] for d in drawing]
#     plt.imshow(I, cmap='gray')
#     ns = len(drawing)

if __name__ == '__main__':
    img_dir = 'images_background'
    stk_dir = 'strokes_background'
    nreps = 20 # number of renditions for each character
    nalphebet = 5 # number of alphabets to show

    # get the folder name:
    alphabet_names = [a for a in os.listdir[img_dir] if a[0] != '.']
    # choose random alphabet:
    alphabet_names = random.sample(alphabet_names, nalphebet)

    # for each alphabet 
    for a in range(nalphebet):
        print('generating figure ' + str(a+1) + ' of ' + str(nalphebet))
        alpha_name = alphabet_names[a]

        # choose a random character from the alphabet 