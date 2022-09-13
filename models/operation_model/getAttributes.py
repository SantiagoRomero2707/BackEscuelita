# Clase que obtiene los atributos del modelo mapeado directamente del ORM.

class GetAttribModel:
    def __init__(self, model_object):
        self.model_object = model_object

    def field_owns(self):

        getter = self.model_object.get(19)
        Dict_attr_model = vars(getter)
        Value = Dict_attr_model['__table__']
        Hello = vars(Value)
        Values = Hello['columns']

        columnas = dict(Values)
        attributes = []
        for key in columnas.keys():
            attributes.append(key)

        # field own or atomic
        diccionarioeval = {}
        for atributoColumna in attributes:
            busquedaColumna = columnas[atributoColumna].__dict__
            evaluarForanea = busquedaColumna['foreign_keys']
            evaluarPrimaria = busquedaColumna['primary_key']
            # print(type(evaluarPrimaria))

            if evaluarPrimaria == True:
                diccionarioeval[atributoColumna] = 2  # print("Es llave primaria")
            else:
                if evaluarForanea:
                    diccionarioeval[atributoColumna] = 0  # print("Es foranea")
                else:
                    diccionarioeval[atributoColumna] = 1  # print("Es un campo propio")
        return diccionarioeval

    # define si la tabla es fuerte o débil
    def get_all_attrib(self):
        search = "ID_PAIS"
        # for j in range(len(model)):
        # print(model, "verificando si es debil o fuerte")
        getter = self.model_object
        Dict_attr_model = vars(getter)
        Value = Dict_attr_model['__table__']
        Hello = vars(Value)

        Values = Hello['foreign_keys']
        if Values:
            return True  # print('contiene') por lo tanto es verdad que es una tabla débil.
        else:
            return False  # print('Nada') por lo tanto es falso que sea una tabla débil, es decir, es una tabla fuerte.

    # retorna el id del campo con la tabla a consultar
    def primary_key(self, find):
        search = find
        for j in range(len(self.model_object)):

            getter = self.model_object.get(j)

            Dict_attr_model = vars(getter)
            Value = Dict_attr_model['__table__']
            Hello = vars(Value)

            Values = Hello['primary_key']
            varAttrib = Values.columns

            for i in dir(varAttrib):
                if not i.startswith('_') and not i.startswith('metadata'):
                    var = vars(varAttrib[i])
                    evaluation = var['primary_key']
                    if i == search:
                        print('\n', 'is ok', (j+1), getter, i, '\n')
                        return getter
                    else:
                        continue
