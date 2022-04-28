import pandas as pd

class Data_loader:

    """ 
    This class defined to retrive the data from source or traning

    """
    def __init__(self,file_object,logging_message):
        self.training_file = 