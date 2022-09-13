class Retrieve(object):

    def __init__(self, model_db, connection, id_record):
        self.model_db = model_db
        self.builder_query = connection.query(self.model_db)
        self.id_record = id_record

    def retrieve_all_records(self):
        # Retrieve all records simile SQl = Select * from
        all_records = self.builder_query.all()
        return all_records

    def record_by_id(self):
        # SQl clause Where
        # Retrieve with id simile SQL: Where id == variable
        record = self.builder_query.get(self.id_record)
        return record

    def count_records(self):
        # Falta arreglar porque cuando se aplica un filtro debe actualizar también la contabilización de los datos.
        # Retrieve number of records by table simile SQL = Count
        count_records = self.builder_query.count()
        return count_records





"""
import pandas as pd
import json

    def clause_where(self):
        # filter to query Where SQL: Where var_table == sentences
        filterByNameAll = inquire.filter_by(first_last_name='Romero').all()
        filterByNameSingle = inquire.filter_by(first_last_name='Romero').first()
        less_by_one = inquire.filter(Persona.age >= 18).all() # With rule in query

    @staticmethod
    def consultOrm():
        # Consulta ORM y posterior creación de Dataframe
        model = select_modelo.select_model(select_modelo.captureGetModel())

        queryData = pd.read_sql(sql=object_connection.query(model).statement, con=object_connection.bind)
        # Para las columnas o cabeceros internos del Data-table
        columns = json.loads(queryData.to_json(orient="columns"))
        # Para los datos o cuerpo interno del Data-table
        datos = json.loads(queryData.to_json(orient="index"))
        # Representación de objeto JSON a formato HTML
        return [columns, datos]
"""
