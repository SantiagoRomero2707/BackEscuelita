import json
import os


class DatabasePersistence:

    @staticmethod
    def read_persistence():
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        new_path = base_dir+'\logicService\persistence.json'
        with open(new_path) as file:
            data = json.load(file)
        return data



