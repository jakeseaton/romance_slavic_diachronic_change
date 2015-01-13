# -*- coding: utf-8 -*-
"""
Created on Mon Jan  5 17:54:27 2015

@author: jakeseaton
"""

#error smoothing function--stand in for res2pat.c
def smooth((x,y,z)):
    genders = {
        "m":(1,0,0),
        "f":(0,1,0),
        "n":(0,0,1)
    }
    if x == y or y == z or z == x:
        print "there's a tie"
    d = {
        float(x) : "m",
        float(y) : "f",
        float(z) : "n",
    }

    max_gender = d[max(d.keys())]
    return genders[max_gender]      

# build a neural network with
# 330 input nodes 
# 30 hidden nodes
# 3 output nodes
from pybrain.tools.shortcuts import buildNetwork

net = buildNetwork(330, 30, 3)

from pybrain.datasets import SupervisedDataSet

trainingset = SupervisedDataSet(330, 3)

from read_input import convert_to_input

# Get the words with desired outputs, the words with frequencies, and trainer
(test_corpus, frequencies, training_corpus) = convert_to_input('corpus.csv')

# training_corpus is an array of tuples. Each tuple contains the numerical repr
# of each word, and the desired output, in a random order.
for (x,y) in training_corpus:
    trainingset.addSample(x,y)
    
# Now train the network
from pybrain.supervised.trainers import BackpropTrainer

trainer = BackpropTrainer(net, trainingset)

# train it for one epoch. 
#This function returns a double proportional to the error.
# can also trainUntilConvergence() which returns a tuple containing the errors
#for each epoch
# can do three generations with the following line of code:
# for x in range(0,3):
error = trainer.train()
print error

counter = 0
# now use it
results = {}
# load in the test corpus. This is an array of (330) tuples
for (word, gender) in test_corpus:
    result = smooth(tuple(net.activate(word)))
    results.update({word: result})
    if result == gender:
        counter += 1
    # we can check accuracy here
    # activate returns an array of the outputs. It will be a 1x3 array
    # we want a 3-tuple, so we apply the conversion function
    # Then we apply the smoothing function
    # we append the resulting gender tuple results 
print ("Accuracy: %s" % (counter/len(test_corpus)))
print results

# Now we can redo it for another generation using the results as the test_corpus
# and change frequencies accordingly