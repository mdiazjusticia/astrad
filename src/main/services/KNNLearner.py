import numpy as np
import util
import operator

def getNeighbors(trainingSetX, trainingSetY, testInstance, k):
        distances = []
        length = len(testInstance)-1
        for x in range(len(trainingSetX)):
            dist = util.euclideanDistance(testInstance, trainingSetX[x], length)
            distances.append((trainingSetX[x], trainingSetY[x], dist))
        distances.sort(key=operator.itemgetter(2))
        neighbors = []
        for x in range(k):
            neighbors.append((distances[x][0], distances[x][1]))
        return neighbors

def getResponse(neighbors, k):
    response = 0
    for x in range(len(neighbors)):
        response += neighbors[x][1]

    response /= k

    return response

class KNNLearner(object):

    def __init__(self, k = 3, verbose = False):
        self.k = k
        pass

    def addEvidence(self,dataX,dataY):
        """
        @summary: Add training data to learner
        @param dataX: X values of data to add
        @param dataY: the Y training values
        """
        # build and save the model
        self.dataX, self.dataY = dataX, dataY

    def query(self,points):
        """
        @summary: Estimate a set of test points given the model we built.
        @param points: should be a numpy array with each row corresponding to a specific query.
        @returns the estimated values according to the saved model.
        """
        predictions = []
        for x in range(len(points)):
            neighbors = getNeighbors(self.dataX, self.dataY, points[x], self.k)
            result = getResponse(neighbors, self.k)
            predictions.append(result)
        return predictions

if __name__=="__main__":
    print "the secret clue is 'zzyzx'"