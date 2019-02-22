from sklearn.neural_network import MLPClassifier

class MatrixPerceptron(MLPClassifier):
    """
    This class converts an MLP classifier to generate matrix transformations
    trained on vector-field datasets.
    This class should complete the following:
        - train a matrix transformation between an nxn input matrix to mxm output matrix
        - reject unstandard variables
    """
    _persist_methods = []
    
    def __init__(self, persister):
        self._persister = persister
    
    def __getattr__(self, attribute):
        if attribute in self._persist_methods:
            return getattr(self._persister, attribute)
    