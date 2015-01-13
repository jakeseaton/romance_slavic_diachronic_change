import math
# define a class of neural networks
class NeuralNetwork:
    
    def __init__(self, numInputs, numHidden, numOutput, eta, alpha, max_epochs):
        # parameters
        self.numInputs = numInputs
        self.numHidden = numHidden
        self.numOutput = numOutput
        self.eta = eta
        self.alpha = alpha
        self.max_epochs = max_epochs
        # initialize empty array for inputs
        self.inputs = [0 for x in xrange (numInputs)]
        # initialize array of empty arrays for input to hidden weights
        self.ihWeights = [[0 for x in xrange(numHidden)] for y in xrange(numInputs)]
        # initialize array of empty arrays for hidden to output weights
        self.hoWeights = [[0 for x in xrange(numOutput)] for y in xrange(numHidden)]
        # initialize an empty array for for sums of hidens
        self.ihSums = [0 for x in xrange(numHidden)]
        # initialize empty array for Biases of hiddens
        self.ihBiases = [0 for x in xrange(numHidden)]
        #initlaize empty array for Sums of outputs        
        self.hoSums = [0 for x in xrange(numOutput)]
        # initialize empty array for Biases of outputs 
        self.hoBiases = [0 for x in xrange(numOutput)]
        # initialize empty array for outputs
        self.outputs = [0 for x in xrange(numOutput)]
        # initialize empty array for gradients of outputs
        self.oGrads = [0 for x in xrange(numOutput)]
        # initialize empty array for gradients of hiddens
        self.hGrads = [0 for x in xrange(numHidden)]
        # initialize array of empty arrays corresponding to change in weights from inputs to hidden
        self.ihWeightsDelta = [[0 for x in xrange(numHidden)] for y in xrange(numInputs)]
        # initialize empty array for change in biases for Hiddens.
        self.ihBiasesDelta = [0 for x in xrange(numHidden)]
        # initialize array of empty arrays for change in weights from hidden to outputs
        self.hoWeightsDelta = [[0 for x in xrange(numOutput)] for y in xrange(numHidden)]
        # initialize empty array for change in biases for Outputs
        self.hoBiasesDelta = [0 for x in xrange(numOutput)]
                
    # Sigmoid function conducts the input to hidden computation
    @staticmethod
    def SigmoidFunction (x):
        if x <-45:
            return 0.0
        elif (x > 45.0):
            return 1.0
        else:
            return 1.0/(1.0 + math.exp(-x))

    # Hyperbolic Tangent Function conducts the hidden to output computation
    @staticmethod
    def HTF(x):
        if x < -10:
            return -1
        elif x > 10:
            return 1
        else:
            return math.tanh(x)