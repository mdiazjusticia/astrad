import KNNLearner as knn

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
        learner2 = knn.KNNLearner(k=3, verbose=True)  # create a KNNLearner
        learner2.addEvidence(dataX, dataY)

        #self.learner.addEvidence(dataX, dataY)
        learners = [learner2]
        #for i in range(0, self.bags):
        #    learners.append(self.learner(**self.kwargs))
        self.learners = learners

    def query(self,points):
        """
        @summary: Estimate a set of test points given the model we built.
        @param points: should be a numpy array with each row corresponding to a specific query.
        @returns the estimated values according to the saved model.
        """
        learner = self.learners[0]

        predictions = learner.query(points)
        return predictions

if __name__=="__main__":
    print "the secret clue is 'zzyzx'"