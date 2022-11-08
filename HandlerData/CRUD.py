from .database.operations_database.Retrieve.inquiere import Retrieve
from .database.operations_database.Update.replace import Update
from .database.operations_database.Create.insert import Create
from .database.operations_database.Drop.delete import Drop
from .models.operation_model.selectModel import GetModels
from .connection.conexionDB import Connect


class MethodsDatabase(Retrieve, Create, Drop, Update, Connect, GetModels):
    def __init__(self, **kwargs):
        self.attrib_all = kwargs


        # objeto conexion a la base de datos
        self.object_connection = self.connecting()

        # Information for transaction with database
        self.attrib_crud_methods = self.attrib_all.get('crud_information')  # Datos correspondientes acción del usuario
        for key, value in self.attrib_crud_methods.items():
            if key == 'method_http':
                self.method_http = value
            elif key == 'model_mapped':
                self.id_model_database = value
            elif key == 'request_data':
                self.instances_model = value
            elif key == 'id_record_database':
                self.id_record_database = value

        # Obtener modelo base de datos
        GetModels.__init__(self, self.id_model_database)
        self.model_db = self.select_model()

        Create.__init__(self, self.model_db, self.instances_model,
                        self.object_connection)  # Inheritance from class create data

        Retrieve.__init__(self, self.model_db, self.object_connection,
                          self.id_record_database)  # Inheritance from class Retrieve get data

        Update.__init__(self, self.model_db, self.object_connection,
                        self.instances_model, self.id_record_database)  # Inheritance from class Update get data

        Drop.__init__(self, self.model_db, self.object_connection,
                      self.id_record_database)  # Inheritance from class Drop data

    def __repr__ (self):
        return f'{self.model_db}' \
               f'\n {self.id_model_database}'\
               f'\n {self.instances_model}' \
               f'\n {self.method_http}' \
               f'\n {self.id_record_database}'

    def methods_graphql(self):
        if self.method_http == 'Query_Filter':
            data_single = self.record_by_id()
            return data_single
        elif self.method_http == 'Query':
            all_records = self.retrieve_all_records()
            return all_records
        elif self.method_http == 'Mutation-Drop':
            drop_data = self.drop_data()
            return f'Okey {drop_data}'
        elif self.method_http == 'Mutation-Create':
            create_data = self.insert_data()
            return f'Okey {create_data}'
        elif self.method_http == 'Mutation-Update':
            update_record = self.update_data()
            return f'Okey {update_record}'
        else:
            return 'ESE METODO HTTP NO EXISTE O NO ESTÁ REGISTRADO, COMUNIQUESE CON EL ADMIN'
