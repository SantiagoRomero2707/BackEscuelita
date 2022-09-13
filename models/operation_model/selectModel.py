from models.base_models.base import MappingAbstract
from flask.globals import request


class GetModels(object):
    def __init__(self, id_model):
        self.id_model = id_model



    def select_model(self):
        models = MappingAbstract.object_model()
        modelSelect = models.get(self.id_model)
        return modelSelect

    # @staticmethod
    # def get_model():
        # valor = request.args.get("type")
        # if valor is None:
            # key_table = None
            # return key_table
        # else:
            # key_table = int(valor)
        # return key_table

