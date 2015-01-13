import Training
import NN
import randomnet

# Number of nodes
I = 20
H = 40
O = 12
# Speed of convergence
eta = 1 
# Momentum
alpha = .4 
# Maximum iterations
epochs = 15000 

# Weight interval
wl = 0
wu = .2
# Bias Interval
bl = -3
bu = -1
# Inputs Interval
il = 0 
iu = .2
# Outputs Interval
ol = -.5
ou = .2

def main():
    # Create a neural network
    net = NN.NeuralNetwork(I, H, O, eta, alpha, epochs)
    # Create a training set. In this case, a random one.
    trainingset = randomnet.randomtrainingset(net, wl, wu, bl, bu, il, iu, ol, ou)
    # Train the network on the set.
    trainednet = Training.train(net, trainingset)
    print "It was supposed to converge to %s\n" % trainingset.outputs
    print "The network is trained!\n"
    # compute outputs at the command line
    while True:
    	print "What are your %s inputs?" % trainednet.numInputs
    	# get user input
        inputs = map(float, raw_input("They must be between %s and %s\n" % (il, iu)).split())
    	# it must match the number of input nodes.
        if len(inputs) != trainednet.numInputs:
    		print "Wrong number of inputs. Start Over\n"
    		break
    	# insert into start of the network
        trainednet.inputs = inputs
        # push through
    	outputs, x, y = Training.ComputeOutputs(trainednet)
        # print result
    	print "The outputs are %s\n" % (map(randomnet.trunc2,outputs))
   	
main()
