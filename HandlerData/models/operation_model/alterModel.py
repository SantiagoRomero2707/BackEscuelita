from models.base_models.base import Mapping_Abstract
from sqlalchemy.sql.schema import ColumnDefault
import inspect

class Modify_Models:

    @staticmethod
    def overview_class(self, opcion):
        print(opcion)
        # print(self, "Se alterará el modelo para la inserción de datos")
        a = Mapping_Abstract.object_model()
        getter = a.get(19)  # Se ingresa y mapea en un diccionario la clase en general con sus atributos y métodos

        Dict_attr_model = vars(getter)

        Value = Dict_attr_model['__table__']
        Hello = vars(Value)

        Values = Hello['columns']
        listOfTuples = inspect.getmembers(Values)
        #pprint(listOfTuples)

        nomFields = []
        for i in range(len(listOfTuples)):
            for j in listOfTuples[i]:
                if not str(j).startswith('_') and not str(j).startswith('<') and not str(j).startswith(
                        'None') and not str(j).__contains__("."):
                    nomFields.append(j)

        # print(nomFields)
        # print(len(nomFields))

        accountant = 0
        while accountant < len(nomFields):
            NomColumn = ""
            Column = ""
            dataInitial = nomFields[accountant]
            # print(dataInitial)
            for i in range(len(listOfTuples)):
                for j in range(len(listOfTuples[i])):
                    evaluation = listOfTuples[i][j]
                    if evaluation == dataInitial:
                        NomColumn = listOfTuples[i][j]
                        Column = listOfTuples[i][j + 1]
                        accountant += 1
                    else:
                        continue
            # print("Ok", NomColumn, Column, "Iteración ", accountant)
            # pprint(vars(Column))
            value = dict(self).get(NomColumn)
            final = vars(Column)
            final['default'] = ColumnDefault(value)  # print("Es una consulta de cambio de valores")
            #if dict(self).get('querydata'):
            #else:
                #final['default'] = None  # print("Es una inserción de datos y por lo tanto debe ser borrada")
            # print(pprint(final), '\n')
        # pprint(listOfTuples)
        return getter
