import Training
import random
import NN

# truncates a float f to 2 decimal places and returns the truncated float
def trunc2(f):
    slen = len('%.2f' % f)
    return float(str(f)[:slen])
    
# returns a random trainingset for a provided neural network
def randomtrainingset(net, weight_l, weight_u, bias_l, bias_u, input_l, input_u, output_l, output_u):
    randomset = Training.trainingset(net)
    print "Randomly training a %s by %s by %s Neural Network" % (net.numInputs, net.numHidden, net.numOutput)
    # Compute the number of weights needed
    weights_needed = net.numHidden * (net.numInputs + net.numOutput)
    weights_list = [trunc2(random.uniform(weight_l, weight_u)) for x in xrange(weights_needed)]
    
    randomset.weights = weights_list

    # compute the number of biases needed
    biases_needed = net.numHidden + net.numOutput
    biases_list = [trunc2(random.uniform(bias_l, bias_u)) for x in xrange(biases_needed)]    
    
    randomset.biases = biases_list
    
    randomset.wandb = weights_list + biases_list
    print "Weights and Biases: %s\n" % randomset.wandb
    
    # get inputs
    inputs = [trunc2(random.uniform(input_l, input_u)) for x in xrange(net.numInputs)]
    print "Inputs: %s\n" % inputs
    randomset.inputs = inputs
    
    # get outputs
    outputs = [trunc2(random.uniform(output_l, output_u)) for x in xrange(net.numOutput)]
    print "Outputs: %s\n" % outputs 
    randomset.outputs = outputs
    return randomset

# returns a net with a random set of parameters
def randomnet(max_nodes, eta_l, eta_u, alpha_l, alpha_u, epochs_l, epochs_u):
    # random number ofinput nodes 
    input_nodes = random.randint(1,max_nodes)
    print "%s input nodes\n" % input_nodes
    # random number of hidden nodes
    hidden_nodes = random.randint(1,max_nodes)
    print "%s hidden nodes\n" % hidden_nodes
    # random number of output nodes
    output_nodes = random.randint(1,max_nodes)
    print "%s output nodes\n" % output_nodes

    # random eta
    eta = random.uniform(eta_l, eta_u)
    print "eta is %s\n" % eta
    
    # random alpha
    alpha = random.uniform(alpha_l, alpha_u)
    print "alpha is %s\n" % alpha

    # random epochs
    epochs = random.randint(epochs_l, epochs_u)
    print "%s max epochs\n" % epochs

    return(NN.NeuralNetwork(input_nodes, hidden_nodes, output_nodes, eta, alpha, epochs))
    
