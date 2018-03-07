import numpy as np

#and, or,  andnot have same single layered structure so a parent base class is used for them

#netinput is w1*x1+w2*x2 which is compared with respective threshold
#Xor is multilayered in MPitt so parent class concept (which is used below)  won't be valid,
#hence is solved otherwise


class MPitt:
    inputPattern = np.array([[1, 1], [1, 0], [0,1], [0, 0]], 'i')

    def __init__(self, thresholdval, w1, w2):
        self.threshold = thresholdval
        self.w1 = w1
        self.w2 = w2
        self.weight = np.array([[self.w1], [self.w2]])

    def printNetwork(self):
        inputY = self.inputPattern
        for item in inputY:
            inputvec = np.array(item)
            total = inputvec.dot(self.weight)
            if total >= self.threshold:
                print("{}  {}".format(item, 1))
            else:
                print("{}  {}".format(item, 0))


class AND (MPitt):
    def __init__(self):
        MPitt.__init__(self, 4, 2, 2)


class OR (MPitt):
    def __init__(self):
        MPitt.__init__(self, 2, 2, 2)

class ANDNOT (MPitt):
    def __init__(self):
        MPitt.__init__(self, 2, 2, -1)
print("And network: ")
andNet = AND()
andNet.printNetwork()

print("OR network: ")
orNet = OR()
orNet.printNetwork()

print("ANDNOT network: ")
andNotNet = ANDNOT()
andNotNet.printNetwork()


class XOR:
    inputPattern = np.array([[1, 1], [1, 0], [0, 1], [0, 0]], 'i')
    threshold = 0

    def __init__(self):
        self.threshold = 2

    def printNetwork(self):
        weight1 = np.array([[2], [-1]])
        weight2 = np.array([[-1], [2]])
        weightzy = np.array([[2], [2]])
        inputY = self.inputPattern
        for item in inputY:
            inputvec = np.array(item)
            z1 = inputvec.dot(weight1)
            z2 = inputvec.dot(weight2)
            if z1 >= self.threshold:
                z1 = 1
            else:
                z1 = 0
            if z2 >= self.threshold:
                z2 = 1
            else:
                z2 = 0
            yin = np.array([z1, z2])
            total = yin.dot(weightzy)
            if total >= self.threshold:
                print("{}  {}".format(item, 1))
            else:
                print("{}  {}".format(item, 0))




print("XOR network: ")
xorNet = XOR()
xorNet.printNetwork()
