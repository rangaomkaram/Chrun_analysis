import os
import pickle
import shutil

class file_operations:

    """
    This class is used for saving the prediction models after training and load them.

    written by : Ranga omkaram

    
    
    """
    def __init__(self,file_object,logging_message):
        self.file_object = file_object
        self.logging_message = logging_message
        self.model_directory = "telecom_Chrun_Analysis/Model_Building/"

    def models_saved(self,model,model_filename):
        """
        Method Name: Save_Model
        Description : Save the model to file_directory
        output : model file saved in the form of .h5 / sav

        Written : Rangasesha
        Revision : None 
        """
        self.logging_message.log(self.file_object,"Enter the modelssaved method of the file_operations class ")
        try:
            path = os.path.join(self.model_directory,model_filename) # creating the separate directory for each cluster
            if os.path.isdir(path): # removing if any pervious models are exist 
                shutil.rmtree(self.model_directory)
                os.makedirs(path)
            else:
                os.makedirs(path)
            with open(path + '/' + model_filename +'.sav', "wb" )as f:
                pickle.dump(model,f) # saving the model to .sav file
            self.logging_message.log(self.file_object,
                                'File model as '+model_filename+'saved. models_saved of the  model_finding class')
            return "Sucessfully saved the model file in format of .sav"

        except Exception as e:
            self.logging_message.log(self.file_object,
                                     "Exception in model_saved method of model_finding class")
            self.logging_message.log(self.file_object,
                                     "Model file "+model_filename+" could not be saved. Exicted models_saved method of model_finding class")
                                     
            raise Exception()                         




                       
