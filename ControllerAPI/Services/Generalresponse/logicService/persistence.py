import json
import os


class DatabasePersistence:

    @staticmethod
    def write_persistence(result_chocolate):
        print(result_chocolate, 'Persistencia')
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        new_path = base_dir+'\logicService\persistence.json'
        data = {'resultTotalChocolate': []}
        data['resultTotalChocolate'].append(
            {
                'result': result_chocolate
            })
        file = open(new_path, "w")
        json.dump(data, file, indent=4)
        file.close()

    @staticmethod
    def read_persistence():
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        new_path = base_dir+'\logicService\persistence.json'
        with open(new_path) as file:
            data = json.load(file)
        for value in data['resultTotalChocolate']:
            result = value
            return result

