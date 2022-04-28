from datetime import datetime
from msilib.schema import Class

class App_Logger:
    def __init__(self):
        pass

    def logging(self,logging_message,file_object):
        self.now = datetime.now()
        self.date = self.now.date()
        self.current_time = self.now.strftime("%H:%M:%S")
        file_object.write(
            str(self.date) + "/" + str(self.current_time) + "\t\t" + logging_message +"\n")

