# from BackEscuelita.database.operations_database.Retrieve.inquiere import Retrieve


class Update(object):
    def __init__(self,  model_db, connection, data_update, id_db_record):
        print(model_db)
        self.builder_query = connection.query(model_db)  # Query o consulta en la db

        self.instance_from_db = self.builder_query.get(id_db_record)  # Instancia del objeto de tipo consulta realizado
        self.data_update = data_update # Data for update  # dato para reemplazar
        self.connection = connection

    def update_data(self):
        # print(f'builder query{self.builder_query}')
        # print(f'instance {self.instance_from_db}')
        # print (f'data_update: {self.data_update}')
        # print(f'data updates it´s works :D')
        if not self.data_update:
            # print('No hay datos para actualizar')
            return 'None'
        else:
            # print('tiene datos para actualizar')
            for key, value in self.data_update.items():
                setattr(self.instance_from_db, key, value)
            # print (f'instance {self.instance_from_db}')
            return self.connection.commit()
