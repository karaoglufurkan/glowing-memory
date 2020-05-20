import os
import json
from shutil import copyfile
from shutil import move

class Categorization:
    def __init__(self, source_path, target_path):
        self.config = self.get_config()
        self.source_path = source_path
        self.target_path = target_path

    def create_folders(self,):
        [os.mkdir(os.path.join(self.target_path, f)) for f in self.config]

    def get_config(self,):
        with open("config.json", "r") as config_reader:
            return json.loads(config_reader.read())

    def categorize(self,):
        for walk in os.walk(self.source_path):
            for file_name in walk[2]:
                # copyfile(os.path.join(walk[0], file_name), os.path.join(self.target_path, self.find_folder_name(file_name), file_name))
                move(os.path.join(walk[0], file_name), os.path.join(self.target_path, self.find_folder_name(file_name)))
    def find_folder_name(self, file_name):
        for i in self.config:
            for j in self.config[i]:
                if file_name.endswith(str(j)):
                    return i   