# from configuration.connection.conexionDB import object_connection


class Drop(object):
    def __init__(self, model_db, connection, id_db_record):
        self.connection = connection
        self.id_db_record = id_db_record
        self.builder_query = connection.query(model_db)  # Query o consulta en la db
        self.instance_from_db = self.builder_query.get(id_db_record)  # Instancia del objeto de tipo consulta realizado

    def drop_data(self):
        """ Drop or Delete """
        record_delete = self.instance_from_db
        # record_delete = inquire.get(id_record_database)
        self.connection.delete(record_delete)
        self.connection.commit()
        return f'record successful delete from sys.databases!! in database id: {record_delete}'

