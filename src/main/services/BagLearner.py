import KNNLearner as knn
import numpy as np

class BagLearner(object):

    def __init__(self, learner = knn.KNNLearner, kwargs = {"k":3}, bags = 20, boost = False, verbose = False):
        self.learner = learner
        self.kwargs = kwargs
        self.bags = bags
        self.boost = boost
        self.verbose = verbose
        pass

    def addEvidence(self,dataX,dataY):
        """
        @summary: Add training data to learner
        @param dataX: X values of data to add
        @param dataY: the Y training values
        """
        # build and save the model
        #learner2 = knn.KNNLearner(k=3, verbose=True)  # create a KNNLearner

        #self.learner.addEvidence(dataX, dataY)
        learners = []
        for i in range(0, self.bags):
            learner = self.learner(**self.kwargs)
            num_samples = len(dataX)
            a = np.random.random_integers(0, num_samples-1, int(0.6*num_samples))
            trainX = dataX[a]
            trainY = dataY[a]
            learner.addEvidence(trainX, trainY)
            learners.append(learner)
        self.learners = learners

    def query(self,points):
        """
        @summary: Estimate a set of test points given the model we built.
        @param points: should be a numpy array with each row corresponding to a specific query.
        @returns the estimated values according to the saved model.
        """
        print len(points)
        predictions = np.zeros(shape=(600, 1))
        print predictions.shape


        for learner in self.learners:
            p = learner.query(points)
            #predictions = np.append(predictions, p, axis=1)
            predictions = np.c_[predictions, p]
            print predictions.shape

        s = predictions.sum(axis=1)
        result = s / self.bags

        return result

if __name__=="__main__":
    print "the secret clue is 'zzyzx'" "the secret clue is 'zzyzx'"