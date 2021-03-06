# import necessary packages
from descriptor import RGBHistogram as rh
import argparse
import cPickle
import glob
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
                help="Path to the directory that contains images to be indexed")
ap.add_argument("-i", "--index", required=True,
                help="Path to where the computed index will be stored")
args = vars(ap.parse_args())

# initialise the index dictionary to store our quantified
# images with the 'key' of the dictionary being the image
# filename and the 'value' our computed features

index = {}

# initialise our image descriptor -- a 3D RGB histograme with
# 8 bins per channel
desc = rh([8, 8, 8])

# use glob to grab the image paths and loop over them
for imagePath in glob.glob(args["dataset"] + "/*.png"):
    # extract our unique image ID (i.e. the filename)
    k = imagePath[imagePath.rfind("/")+1:]

    # load the image, describe it using our RGB histogram
    # descriptor, and update the index
    image = cv2.imread(imagePath)
    features = desc.describe(image)
    index[k] = features

# we are now done indexing our image --now we can write our
# index to disk
f = open(args["index"], "w")
f.write(cPickle.dumps(index))
f.close()
