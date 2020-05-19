import os
import json
from shutil import copyfile

class Categorization:
    def __init__(self, ):
        self.config = self.get_config()
        self.main_directory = os.getcwd() + "/demo_folder"

    def create_folders(self,):
        [os.mkdir(f) for f in self.config]

    def get_config(self,):
        with open("config.json", "r") as config_reader:
            return json.loads(config_reader.read())

    def categorize(self,):
        for walk in os.walk(self.main_directory):
            for file_name in walk[2]:
                copyfile(str(walk[0]) + "/" + str(file_name), str(os.getcwd()) + "/" + str(self.find_folder_name(file_name)) + "/" + str(file_name))

    def find_folder_name(self, file_name):
        for i in self.config:
            for j in self.config[i]:
                if file_name.endswith(str(j)):
                    return i

if __name__ == "__main__":
    cat = Categorization()
    # cat.create_folders()
    cat.categorize()    