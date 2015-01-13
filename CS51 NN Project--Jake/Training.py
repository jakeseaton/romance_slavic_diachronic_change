import math
class trainingset:

    def __init__(self, net):
        # number of needed weights
        self.weights = [0 for x in xrange(net.numHidden * (net.numInputs + net.numOutput))]
        # number of needed biases
        self.biases = [0 for x in xrange(net.numHidden + net.numOutput)]
        # number of needed inputs
        self.inputs = [0 for x in xrange(net.numInputs)]
        # number of needed outputs
        self.outputs = [0 for x in xrange(net.numOutput)]
        self.wandb = self.weights + self.biases

def train(net,tset):
    net.inputs = tset.inputs 
    net.outputs = tset.outputs
    wandb = tset.wandb
    #  fill input to hidden array with initial weights
    for i in xrange(net.numInputs):
        for y in xrange(net.numHidden):
            # print "Currently indexing %s %s" % (i, y)
            # print "The index of wandb is %s" % (i * net.numHidden + y) 
            net.ihWeights[i][y] = wandb[i * net.numHidden + y]
    # fill hidden to output array with initial weights
    for i in xrange(net.numHidden):
        for y in xrange(net.numOutput):
            net.hoWeights[i][y] = wandb[(net.numHidden * net.numInputs) + i * net.numOutput + y]
    # fill input to hidden array with initial biases
    for i in xrange(net.numHidden):
        net.ihBiases[i] = wandb[(net.numHidden * net.numInputs + (net.numHidden * net.numOutput)) + i]
    # fill hidden to output array with initial biases
    for i in xrange(net.numOutput):
        net.hoBiases[i] = wandb[(net.numHidden * net.numInputs + (net.numHidden * net.numOutput))+ net.numHidden + i]
    # conduct iteractions, with specified maximum
    for i in xrange(net.max_epochs):
        # send the data through
        localout, hlocalout,inputstuff = ComputeOutputs(net)
        # use the output to conduct back propogation 
        ComputeBackPropogation(localout, hlocalout, net)
        # update the weights
        ComputeWeightBiasDelta (net, inputstuff)
    current_outputs, x, y = ComputeOutputs(net)
    # print result and return
    print "It converged to %s" % current_outputs
    return net

def ComputeWeightBiasDelta (net,inputstuff):
    # get previous values
    prevdeltih = net.ihWeightsDelta
    prevdeltho = net.hoWeightsDelta  
    prevdelthob = net.hoBiasesDelta
    prevdeltihb = net.ihBiasesDelta
    # update input to hidden weights
    for i in xrange(net.numInputs):
        for x in xrange(net.numHidden):
            # 
            net.ihWeightsDelta[i][x] = net.hGrads[x] * net.eta * net.inputs[i]
            net.ihWeights[i][x] = net.ihWeights[i][x] + net.ihWeightsDelta[i][x] + net.alpha * prevdeltih[i][x]
    # update output to hidden weights
    for i in xrange(net.numHidden):
        for x in xrange(net.numOutput):
            net.hoWeightsDelta[i][x] = net.oGrads[x] * net.eta * inputstuff[i]
            net.hoWeights [i][x] = net.hoWeights[i][x] + net.hoWeightsDelta[i][x] + net.alpha * prevdeltho[i][x]
    # update input to hidden Biases
    for i in xrange(net.numHidden):
        net.ihBiasesDelta[i] = net.eta * net.hGrads[i]
        net.ihBiases[i] = net.ihBiases[i] + net.ihBiasesDelta[i] + net.alpha * prevdeltihb[i]
    # update hidden to output Biases
    for i in xrange(net.numOutput):
        net.hoBiasesDelta[i] = net.eta * net.oGrads[i]
        net.hoBiases[i] = net.hoBiases[i] + net.hoBiasesDelta[i] + net.alpha * prevdelthob[i]

def ComputeBackPropogation(localout, hlocalout, net):
    # compute output gradients
    for i in xrange(net.numOutput):
        net.oGrads[i] = (1 - localout[i]) * ( 1 + localout[i]) * (net.outputs[i] - localout[i])
    # compute hidden gradients
    for x in xrange(net.numHidden):
        sumx = 0
        for i in xrange(net.numOutput):
            sumx = sumx + net.oGrads[i] * net.hoWeights[x][i]
        net.hGrads[x] = (hlocalout[x])*(1 - hlocalout[x])*(sumx)

# Pushes inputs through the network
def ComputeOutputs(net):
    local = [0 for x in xrange(net.numHidden)]
    endresult = [0 for x in xrange(net.numOutput)]
    inputstuff = [0 for x in xrange(net.numHidden)]
    # Push to hidden layer
    for i in xrange(net.numHidden):
        sumi = 0
        for x in xrange(net.numInputs):
            sumi = sumi + net.ihWeights[x][i] * net.inputs[x]
        sumi = sumi + net.ihBiases[i]
        inputstuff[i] = sumi
        local[i] = net.SigmoidFunction(sumi)
    # Push to output layer
    for i in xrange(net.numOutput):
        sumi = 0
        for x in xrange(net.numHidden):
            sumi = sumi + net.hoWeights[x][i]* local[x]
        sumi = sumi + net.hoBiases[i]
        endresult[i] = net.HTF(sumi)
    # print(endresult)
    return endresult, local, inputstuff