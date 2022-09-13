from models.base_models.database_models import Model
from sqlalchemy.ext.declarative import declarative_base


class MappingAbstract(object):

    # Variables of class Mapping Abstract
    dict = {}  # Dictionary that storage the model´s mapping with your respective ID
    Base = declarative_base()  # Mapping of ORM

    @classmethod
    def mapping_model(cls):
        notYetMapping = Model.__subclasses__()
        for i in range(len(notYetMapping)):
            cls.dict[i] = type(str(notYetMapping[i].__name__), (cls.Base, notYetMapping[i]), {})
        return cls.dict

    @classmethod
    def object_model(cls):
        mappingFinal = cls.dict
        if mappingFinal:
            return mappingFinal
        else:
            mappingFinal = cls.mapping_model()
            return mappingFinal
