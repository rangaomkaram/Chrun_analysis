import pandas as pd

class Data_loader:

    """ 
    This class defined to retrive the data from source or traning

    """
    def __init__(self,file_object,logging_object):
        self.training_file = "telecom_Chrun_Analysis/TeleCom_Raw_Data/rawdata.csv"
        self.file_object = file_object
        self.logging_object = logging_object

    def Get_Data(self):
        """
        Method Name : Get_Data
        Description : This method reads the data from raw data source
        Output : Pandas Dataframe
    
        """
        self.logging_object.log(self.file_object,"Getting into the Get_Data Method of the Data_loader class")

        """
        Excepetion Handling 
        """
        try:
            self.data = pd.read_csv(self.training_file)
            self.logging_object.log(self.file_object,
                        "Message : Raw Data is sucessfully loaded using Get_Data method of Data_loader class")
            return self.data

        except Exception as e:
            self.logging_object.log(self.file_object,
                                      "Excepection raise in the Get_Data method of the Data_loader class")
            self.logging_object.log(self.file_object,
                         "loading the Data is Unsuccessful.check the get_data method of the Data_loader class")
            raise Exception()
