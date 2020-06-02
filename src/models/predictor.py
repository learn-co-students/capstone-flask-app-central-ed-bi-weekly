"""
This predictor module is designed for use with Scikit-Learn models.  If you are
using a different library such as TensorFlow or Surprise, the structure will be
similar in terms of loading from a pickle then making a prediction, but some
details will differ
"""
import pickle

def make_prediction(test_value):
    """
    Make a prediction for a given test value by loading a pickled model

    Parameters:
        test_value: an array-like containing a value representing each
        X feature

    Returns:
        A single prediction from the model
    """
    loaded_model = load_sklearn_model()
    # brackets around test_value because sklearn models are expecting to make
    # predictions about a list of records, not just one record
    predictions = loaded_model.predict([test_value])
    # [0] on the results because we only want a single prediction, not a list
    return predictions[0]
    
def load_sklearn_model():
    """
    Load the model from the .pickle file
    
    Returns:
        A fitted sklearn model loaded from a .pickle file
    """
    # path is relative to app.py
    PICKLE_PATH = "src/models/iris_classifier.pickle"
    with open(PICKLE_PATH, "rb") as model_file:
        loaded_model = pickle.load(model_file)
    return loaded_model
