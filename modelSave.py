import pickle

def saves(model):
    '''
        Saves the output from the model into a file
            Parameter:
                model: the model that is being written into a file
            Returns:
                 None
    '''

    with open("model.txt", "wb") as internal_filename:
        pickle.dump(model, internal_filename)


def reads():
    '''
        Reads the saved model from a file
            Parameters:
                None
            Returns:
                model (list of lists): a list of lists containing [P(A), P(B|A), P(C|AB)]
    '''

    with open("model.txt", "rb") as new_filename:
        model = pickle.load(new_filename)

    return model
