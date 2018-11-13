import numpy as np
from numpy import dot
from numpy.linalg import norm
import json
import math

def cosine_similarity(list1, list2):
    return dot(list1, list2) / (norm(list1) * norm(list2))

with open("homework4/dataset.json") as read_file:
	data = json.load(read_file)

vgg_data = np.load("homework4/vgg_rep.npy")
pixel_data = np.load("homework4/pixel_rep.npy")

images_set = data["images"]
train_set = data["train"]
test_set = data["test"]
captions_set = data["captions"]

images_dict = {}
for i in range(len(images_set)):
	images_dict[images_set[i]] = i

with open("vgg.txt", "w") as vgg_file:
	for i in test_set:
		nearest = 0
		value = -2
		for j in train_set:
			cos = cosine_similarity(vgg_data[images_dict[i]], vgg_data[images_dict[j]])
			if cos > value:
				value = cos
				nearest = j
		print "nearest value = " + str(nearest) + " for " + str(i)
		print "index of nearest = " + str(images_dict[nearest])
		print "caption = " + str(captions_set[nearest])
		vgg_file.write(str(captions_set[nearest]) + "\n")

with open("pixel.txt", "w") as pixel_file:
	for i in test_set:
		nearest = 0
		value = -2
		for j in train_set:
			cos = cosine_similarity(pixel_data[images_dict[i]], pixel_data[images_dict[j]])
			if cos > value:
				value = cos
				nearest = j
		print "nearest value = " + str(nearest) + " for " + str(i)
		print "index of nearest = " + str(images_dict[nearest])
		print "caption = " + str(captions_set[nearest])
		pixel_file.write(str(captions_set[nearest]) + "\n")


# Q5.
# with open("./homework4/cnn_dataset.json") as read_file:
# 	data = json.load(read_file)

# print "Pixel Representation"
# print str(cosine_similarity(data["pixel_rep"]["mj1"], data["pixel_rep"]["mj2"]))
# print str(cosine_similarity(data["pixel_rep"]["mj2"], data["pixel_rep"]["cat"]))
# print str(cosine_similarity(data["pixel_rep"]["cat"], data["pixel_rep"]["mj1"]))

# print "VGG Representation"
# print str(cosine_similarity(data["vgg_rep"]["mj1"], data["vgg_rep"]["mj2"]))
# print str(cosine_similarity(data["vgg_rep"]["mj2"], data["vgg_rep"]["cat"]))
# print str(cosine_similarity(data["vgg_rep"]["cat"], data["vgg_rep"]["mj1"]))
